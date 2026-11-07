# -*- coding: utf-8 -*-
"""
嵌入式社区养老服务优化模型 V3

四个问题：
1. 老龄人口预测
2. 服务站选址优化
3. 服务定价优化
4. 敏感性分析

说明：
请将本文件与5个附件Excel放在同一目录运行。

"""

import os
import itertools
import numpy as np
import pandas as pd


ROOT = os.path.dirname(os.path.abspath(__file__))


# =========================
# 数据读取
# =========================

def read_data():

    files = os.listdir(ROOT)

    def find_file(keyword):
        for f in files:
            if keyword in f and f.endswith(".xlsx"):
                return os.path.join(ROOT, f)
        raise FileNotFoundError(keyword)

    # 附件1
    f1 = find_file("附件1")
    pop = pd.read_excel(f1, sheet_name="人口与老人结构", header=1)

    # 自动保留前7列
    pop = pop.iloc[:, :7]
    pop.columns = [
        "小区", "人口", "老人", "自理", "半失能", "失能", "收入"
    ]

    # 附件2
    f2 = find_file("附件2")

    demand = pd.read_excel(
        f2,
        sheet_name="每位老人月均服务需求次数",
        header=1
    )

    income = pd.read_excel(
        f2,
        sheet_name="服务营收及支出",
        header=1
    )

    # 附件3
    f3 = find_file("附件3")

    station = pd.read_excel(
        f3,
        header=1
    )

    station = station.iloc[:, :4]
    station.columns=[
        "规模",
        "建设成本",
        "日固定成本",
        "容量"
    ]

    # 建设成本转换为数字
    station["建设成本"] = (
        station["建设成本"]
        .astype(str)
        .str.extract(r'(\d+\.?\d*)')[0]
        .astype(float)
    )

    # 日固定成本转换
    station["日固定成本"] = (
        station["日固定成本"]
        .astype(str)
        .str.extract(r'(\d+\.?\d*)')[0]
        .astype(float)
    )

    # 容量转换
    station["容量"] = (
        station["容量"]
        .astype(str)
        .str.extract(r'(\d+\.?\d*)')[0]
        .astype(float)
    )

    # 附件4
    f4 = find_file("附件4")

    raw = pd.read_excel(
        f4,
        header=None
    )

    # 自动寻找数字矩阵
    distance = raw.iloc[2:,1:]
    distance = distance.iloc[:10,:10]
    distance = distance.apply(pd.to_numeric)

    # 附件5
    f5 = find_file("附件5")

    satisfaction_rule = pd.read_excel(
        f5,
        header=None
    )

    return pop, demand, income, station, distance, satisfaction_rule



# =========================
# 问题1
# =========================

def population_prediction(pop):

    state = pop[
        ["自理","半失能","失能"]
    ].values.astype(float)


    result=[]

    P=np.array([
        [0.85,0.1,0.05],
        [0,0.85,0.15],
        [0,0,1]
    ])


    for year in range(5):

        state=state.dot(P)

        result.append(
            state.sum(axis=0)
        )


    return pd.DataFrame(
        result,
        columns=[
            "自理老人",
            "半失能老人",
            "失能老人"
        ],
        index=[
            f"第{i}年" for i in range(1,6)
        ]
    )



# =========================
# 问题2
# =========================

def satisfaction(distance):

    if distance<=300:
        return 1
    elif distance<=500:
        return 0.9
    elif distance<=1000:
        return 0.8
    else:
        return 0.6



def location_model(pop, station, distance, budget=120):

    best=None

    for n in range(1,4):

        for loc in itertools.combinations(range(10), n):

            for size in itertools.product(
                range(len(station)), repeat=n
            ):

                cost=sum(
                    station.iloc[i]["建设成本"]
                    for i in size
                )

                if cost>budget:
                    continue


                score=0

                for j in range(10):

                    score+=max(
                        satisfaction(distance.iloc[j,i])
                        for i in loc
                    )*pop.iloc[j]["老人"]


                score/=pop["老人"].sum()


                value=0.4+0.6*score


                if best is None or value>best["目标值"]:

                    best={
                        "位置":[pop.iloc[i]["小区"] for i in loc],
                        "规模":[station.iloc[i]["规模"] for i in size],
                        "成本":cost,
                        "满意度":score,
                        "目标值":value
                    }

    return pd.DataFrame([best])



# =========================
# 问题3
# =========================

def price_model(income):

    result=[]

    for rate in np.arange(0.8,1.21,0.05):

        revenue=0
        cost=0

        for _, row in income.iterrows():

            nums = pd.to_numeric(
                row,
                errors="coerce"
            ).dropna()

            if len(nums) >= 2:
                revenue += nums.iloc[0] * rate

                cost += nums.iloc[1]


        profit=(revenue-cost)/max(cost,1)


        if profit<=0.08:

            result.append(
                {
                    "价格系数":round(rate,2),
                    "利润率":profit
                }
            )


    return pd.DataFrame(result)



# =========================
# 问题4
# =========================

def sensitivity(pop, station, distance):

    result=[]

    for growth in [0.9,1,1.1]:

        temp=pop.copy()

        temp["老人"]=temp["老人"]*growth

        plan=location_model(
            temp,
            station,
            distance
        )

        result.append(
            {
                "老人规模变化":growth,
                "满意度":plan.iloc[0]["满意度"],
                "成本":plan.iloc[0]["成本"]
            }
        )


    for cost_rate in [0.8,1,1.2]:

        temp=station.copy()

        temp["建设成本"]*=cost_rate

        plan=location_model(
            pop,
            temp,
            distance
        )

        result.append(
            {
                "成本变化":cost_rate,
                "满意度":plan.iloc[0]["满意度"],
                "成本":plan.iloc[0]["成本"]
            }
        )

    return pd.DataFrame(result)



# =========================
# 主程序
# =========================

if __name__=="__main__":

    pop,demand,income,station,distance,rule=read_data()

    os.makedirs("result",exist_ok=True)


    p1=population_prediction(pop)
    p1.to_excel("result/问题1人口预测.xlsx")


    p2=location_model(
        pop,
        station,
        distance
    )
    p2.to_excel(
        "result/问题2选址方案.xlsx",
        index=False
    )


    p3=price_model(income)
    p3.to_excel(
        "result/问题3定价方案.xlsx",
        index=False
    )


    p4=sensitivity(
        pop,
        station,
        distance
    )

    p4.to_excel(
        "result/问题4敏感性分析.xlsx",
        index=False
    )


    print("四个问题全部运行完成")