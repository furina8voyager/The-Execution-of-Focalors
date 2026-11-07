# # #第三部分的实验代码
# # import statistics
# # import time
# #
# # from linked_list import LNode
# #
# #
# # class TailLinkedList:
# #
# #     def __init__(self):
# #         self.head = None
# #         self.tail = None
# #         self._length = 0
# #
# #     def get_length(self):
# #         return self._length
# #
# #     def add_first(self, data):
# #         node = LNode(data)
# #         node.next = self.head
# #         self.head = node
# #
# #         if self.tail is None:          # 空表插入第一个节点
# #             self.tail = node
# #         self._length += 1
# #
# #     def add_last(self, data):
# #         node = LNode(data)
# #
# #         if self.head is None:
# #             self.head = self.tail = node
# #         else:
# #             self.tail.next = node      # 直接用尾指针，O(1)
# #             self.tail = node
# #
# #         self._length += 1
# #
# #     def insert(self, index, data):
# #         if index <= 0:
# #             self.add_first(data)
# #             return
# #
# #         if index >= self._length:
# #             self.add_last(data)
# #             return
# #
# #         prev = self.head
# #         for _ in range(index - 1):
# #             prev = prev.next
# #
# #         node = LNode(data)
# #         node.next = prev.next
# #         prev.next = node
# #         self._length += 1
# #
# # def seq_head(n):
# #     data = []
# #     for i in range(n):
# #         data.insert(0, i)              # O(n)：所有元素后移
# #     return data
# #
# # def seq_middle(n):
# #     data = []
# #     for i in range(n):
# #         data.insert(len(data) // 2, i)  # O(n)：中间插入要搬移
# #     return data
# #
# #
# # def seq_tail(n):
# #     data = []
# #     for i in range(n):
# #         data.append(i)                 # 均摊 O(1)
# #     return data
# #
# # def link_head(n):
# #     linked = TailLinkedList()
# #     for i in range(n):
# #         linked.add_first(i)
# #     return linked
# #
# #
# # def link_middle(n):
# #     linked = TailLinkedList()
# #     for i in range(n):
# #         linked.insert(linked.get_length() // 2, i)
# #     return linked
# #
# #
# # def link_tail(n):
# #     linked = TailLinkedList()
# #     for i in range(n):
# #         linked.add_last(i)
# #     return linked
# #
# #
# # def bench(fn, n, repeat=5):
# #     times = []
# #
# #     for _ in range(repeat):
# #         start = time.perf_counter()
# #         result = fn(n)                 # 保留结果，避免计时期间被回收
# #         elapsed = time.perf_counter() - start
# #         times.append(elapsed)
# #         del result
# #
# #     return statistics.median(times)
# #
# # def main():
# #     cases = [
# #         ("头部插入", 1000, seq_head, link_head),
# #         ("头部插入", 10000, seq_head, link_head),
# #         ("头部插入", 50000, seq_head, link_head),
# #         ("中间插入", 1000, seq_middle, link_middle),
# #         ("中间插入", 10000, seq_middle, link_middle),
# #         ("中间插入", 50000, seq_middle, link_middle),
# #         ("尾部插入", 1000, seq_tail, link_tail),
# #         ("尾部插入", 10000, seq_tail, link_tail),
# #         ("尾部插入", 50000, seq_tail, link_tail),
# #     ]
# #
# #     seq_head(50)
# #     link_head(50)
# #
# #     print(f"{'场景':<8}{'数据量':>10}{'顺序表(s)':>16}{'单链表(s)':>16}")
# #     print("-" * 52)
# #
# #     for name, n, seq_fn, link_fn in cases:
# #         seq_time = bench(seq_fn, n)
# #         link_time = bench(link_fn, n)
# #         print(f"{name:<8}{n:>10}{seq_time:>16.6f}{link_time:>16.6f}")
# #
# #     print("\n注：单链表为带尾指针版本，尾插为 O(1)。")
# #
# #
# # if __name__ == "__main__":
# #     main()
# import statistics
# import time
#
# from quen import SequentialQueue, LinkQueue
#
#
# def seq_ops(n):
#     q = SequentialQueue(n + 1)
#
#     for i in range(n):
#         q.enqueue(i)
#
#     for _ in range(n):
#         q.dequeue()
#
#     return q
#
#
# def link_ops(n):
#     q = LinkQueue()
#
#     for i in range(n):
#         q.enqueue(i)
#
#     for _ in range(n):
#         q.dequeue()
#
#     return q
#
#
# def bench(fn, n, repeat=5):
#     times = []
#
#     for _ in range(repeat):
#         start = time.perf_counter()
#         result = fn(n)
#         elapsed = time.perf_counter() - start
#         times.append(elapsed)
#         del result
#
#     return statistics.median(times)
#
#
# if __name__ == "__main__":
#     # 热身
#     seq_ops(1000)
#     link_ops(1000)
#
#     print(f"{'数据量':>10}{'顺序循环队列(s)':>20}{'链式队列(s)':>18}")
#     print("-" * 50)
#
#     for n in (10000, 100000, 500000):
#         t_seq = bench(seq_ops, n)
#         t_link = bench(link_ops, n)
#         print(f"{n:>10}{t_seq:>20.6f}{t_link:>18.6f}")
import statistics
import time


def hanoi_count(n):
    """只统计步数，不打印，用于性能测试。"""
    if n == 0:
        return 0
    return hanoi_count(n - 1) + 1 + hanoi_count(n - 1)


def bench(fn, n, repeat=5):
    times = []
    steps = 0

    for _ in range(repeat):
        start = time.perf_counter()
        steps = fn(n)
        elapsed = time.perf_counter() - start
        times.append(elapsed)

    return statistics.median(times), steps


if __name__ == "__main__":
    # 热身
    hanoi_count(5)

    print(f"{'n':>4}{'总移动步数':>14}{'运行时间(s)':>16}{'2^n-1':>14}{'是否一致':>10}")
    print("-" * 62)

    for n in (5, 10, 15, 20):
        elapsed, steps = bench(hanoi_count, n)
        expected = 2 ** n - 1
        same = "是" if steps == expected else "否"
        print(f"{n:>4}{steps:>14}{elapsed:>16.6f}{expected:>14}{same:>10}")