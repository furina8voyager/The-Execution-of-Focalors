class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
#要一个 顺序 循环 队列类，牺牲一个存储单元
class SequentialQueue:
#初始化队列
    def __init__(self,capacity = 10):
        self.data = [None for _ in range(capacity+1)]
        self.first = 0
        self._next = 0
        self.length = 0
#判断空
    def is_empty(self) -> bool:
        return self.first == self._next
#返回队列中元素个数 : 维护一个计数器 cont O(1)
    def size(self) -> int:
        return self.length
#入队操作，元素加入队尾 :队满时返回 False，入队成功返回 True
#取模物理总长度，不是我的逻辑增加长度
    def enqueue(self,item) -> bool:
        if (self._next + 1) % len(self.data) == self.first:
            return False
        self.data[self._next] = item
        self._next = (self._next + 1) % len(self.data)
        self.length += 1
        return True
#出队操作，移除并返回队头元素,队空时返回 None
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            item = self.data[self.first]
            self.data[self.first] = None
            self.first = (self.first + 1) % len(self.data)#前进！！！
            self.length -= 1
            return item
#获取队头元素，不移除	队空时返回 None
    def get_front(self):
        if self.is_empty():
            return None
        else:
            return self.data[self.first]
#清空整个队列	释放所有元素引用
#循环队列判空只看 first == _next,把两个指针都归 0，队列立刻变空
##漏把 _next 归零了
    def clear(self):
        self.data = [None for _ in range(len(self.data))]
        self.first = 0
        self._next = 0
        self.length = 0
#按队头到队尾顺序返回元素列表,用于测试验证结果
#我不应该又忘记设置临时变量
    def to_list(self) -> list:
        result = []
        index = self.first
        for i in range(self.length):
            result.append(self.data[index])
            index = (index + 1) % len(self.data)
        return result

#链式队列，没有容量 问题
#两类必须统一接口规范，方法名与参数严格对应，确保可互换测试
class LinkQueue:
#初始化空队列
    def __init__(self,capacity = 10):
        self.first = None
        self._next = None
        self.length = 0
#判断队列是否为空
    def is_empty(self) -> bool:
        return self.first is None
#判断队列是否为空
    def size(self) -> int:
        return self.length
#入队操作，元素加入队尾
    def enqueue(self,item) -> bool:
        node = Node(item)
        if self.first is None:
            self.first = self._next = node
        else:
            self._next.next = node
            self._next = node
        self.length += 1
        return True
#出队操作，移除并返回队头元素
    def dequeue(self):
        if self.is_empty():
            return None
        node = self.first
        self.first = node.next
        node.next = None
        if self.first is None:
            self._next = None
        self.length -= 1
        return node.data
#获取队头元素，不移除
    def get_front(self):
        if self.is_empty():
            return None
        return self.first.data
#清空整个队列
    def clear(self):
        self.first = None
        self._next = None
        self.length = 0
#按队头到队尾顺序返回元素列表
    def to_list(self) -> list:
        result = []
        index = self.first
        while index is not None:
            result.append(index.data)
            index = index.next
        return result

#不牺牲一个存储单元,进阶第一题
class SequentialQueueOptimized:
    def __init__(self, capacity=10):
        self.data = [None for _ in range(capacity)]  # 不额外留空位
        self.first = 0
        self._next = 0
        self.length = 0

    def is_empty(self) -> bool:
        return self.length == 0

    def size(self) -> int:
        return self.length

    def enqueue(self, item) -> bool:
        if self.length == len(self.data):
            return False
        self.data[self._next] = item
        self._next = (self._next + 1) % len(self.data)
        self.length += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.data[self.first]
        self.data[self.first] = None
        self.first = (self.first + 1) % len(self.data)
        self.length -= 1
        return item

    def get_front(self):
        if self.is_empty():
            return None
        return self.data[self.first]

    def clear(self):
        self.data = [None for _ in range(len(self.data))]
        self.first = 0
        self._next = 0
        self.length = 0

    def to_list(self) -> list:
        result = []
        index = self.first
        for i in range(self.length):
            result.append(self.data[index])
            index = (index + 1) % len(self.data)
        return result
#队满判断方案对比：
#牺牲单元法：
#    空队列 first == _next；
#    队满 (self._next + 1) % len(self.data) == self.first。
#    优点：实现简单，不需要额外计数器。
#    缺点：容量为 N 时实际需要 N+1 个空间，浪费一个槽位。
#
#计数器法：
#    空队列 length == 0；
#    队满 length == capacity。
#    优点：不浪费槽位，判空/判满/length 都是 O(1)。
#    缺点：每个队列多维护一个整数 length。
#
#标记法：
#    first == _next 时，用 tag 记录上一次是入队还是出队：
#    tag = 0 表示上次是出队，队空；tag = 1 表示上次是入队，队满。
#    优点：不浪费槽位，也不需要 length 计数。
#    缺点：每次入队/出队都要正确维护 tag，漏改一次就会把空/满判断弄反。

#汉诺塔问题递归求解(进阶的第二道题)
step = 0
def hanoi_recursive(n, source, helper, target):
    global step
    if n <= 0:
        return 0
    if n==1:
        step += 1
        print(f"第{step}步：将圆盘从 {source} 移到 {target}")
        return 1
    step1 = hanoi_recursive(n - 1, source, target, helper)
    step += 1
    print(f"第{step}步：将圆盘从 {source} 移到 {target}")
    step2 = 1
    step3 = hanoi_recursive(n - 1, helper, source, target)
    return step1 + step2 + step3

#汉诺塔移动序列的队列缓存(进阶的第三道题)
def hanoi_recursive_2(n, source, helper, target):
    if n<=0:
        return 0
    q = LinkQueue()
    def move(a,b,c,d):
        if a == 0:
            return 0
        move(a-1,b,d,c)
        q.enqueue(f"将圆盘从 {b} 移到 {d}")
        move(a-1,c,b,d)
    move(n,source,helper,target)
    step = 0
    while not q.is_empty():
        step += 1
        print(f"第{step}步：{q.dequeue()}")
    return step

#拓展2
class PriorityNode:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self.length

    def enqueue(self, item, priority) -> bool:
        node = PriorityNode(item, priority)
        # 空队列，或者新节点优先级最高，插在头部
        if self.head is None or priority < self.head.priority:
            node.next = self.head
            self.head = node
        else:
            cur = self.head
            # 找到最后一个 priority <= 新优先级的节点
            # 用 <= 保证同优先级时，先入队的排在前面
            while cur.next is not None and cur.next.priority <= priority:
                cur = cur.next
            node.next = cur.next
            cur.next = node
        self.length += 1
        return True

    def dequeue(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        node.next = None
        self.length -= 1
        return node.data

    def get_front(self):
        if self.head is None:
            return None
        return self.head.data

    def clear(self):
        self.head = None
        self.length = 0

    def to_list(self) -> list:
        result = []
        cur = self.head

        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result

    def to_priority_list(self) -> list:
        result = []
        cur = self.head

        while cur is not None:
            result.append((cur.priority, cur.data))
            cur = cur.next

        return result
#区别：
#普通队列只看到达顺序；
#栈只看最后进入的顺序；
#优先级队列看优先级，到达顺序只在优先级相同时起作用。

#实际应用场景
# 操作系统进程调度
# 高优先级进程先获得 CPU，低优先级进程后执行。
# 医院急诊分诊
# 病情更紧急的病人优先就诊，而不是单纯按到达顺序。