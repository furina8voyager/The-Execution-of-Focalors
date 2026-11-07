#先保存后继，再改指针；先接新链，再断旧链；删节点先跨过，再清引用
class LNode:
    ##定义一个链表
    def __init__(self,data  = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    #初始化
    def __init__(self):
        self.head = None
        self._length = 0
    #判断是否为欸空的
    def is_empty(self) -> bool:
        return self.head is None
    #判断当前链表多长
    def get_length(self) -> int:
        return self._length

    #头插入
    def add_first(self,data):
            new_node = LNode(data)
            new_node.next = self.head
            self.head = new_node
            self._length += 1
            return new_node

    #末尾插入
    def add_last(self,data):
            new_node = LNode(data)
            if self.head is None:
                self.head = new_node
            else:
                a = self.head
                while a.next is not None:
                    a = a.next
                a.next = new_node
            self._length += 1
            return new_node

    #删除指定位置的元素
    def remove_by_index(self,index: int):               #我应该给头指针创建一个临时变量，不然头指针会丢失，链表就丢了
        if index < 0 or index >= self._length:
            return None
        if index == 0:
            a = self.head                 #临时变量仅是被赋了和头指针一样的地址值头删时，self.head 必须重新赋值，不能只改局部变量 a
            self.head = a.next
        else:
            b = self.head
            for i in range(index - 1):
                b = b.next
            a = b.next
            b.next = a.next
        a.next = None                                       #清空断开节点
        self._length -= 1
        return a.data

          #在指定索引位置插入节点
    def insert(self,index: int, data) -> bool:
        if index < 0 or index > self._length:
            return False
        if index == 0:
            self.add_first(data)
            return True
        elif index == self._length:
            self.add_last(data)
            return True
        else:
            new_node = LNode(data)
            a = self.head
            for i in range(index - 1):
                a = a.next
            new_node.next = a.next
            a.next = new_node
            self._length += 1
        return True

    #删除第一个值匹配的节点
    def remove_by_value(self, data) -> bool:
        a = None
        b = self.head
        while b is not None:
            if b.data == data:
                if a is None:
                    self.head = b.next
                else:
                    a.next = b.next
                b.next = None
                self._length -= 1
                return True
            a = b
            b = b.next
        return False

    #获取指定索引位置的数据
    def get(self,index: int):
        if index < 0 or index >= self._length:
            return None
        else:
            a = self.head
            for i in range(index):
                a = a.next
        return a.data

    #查找值对应的第一个索引
    def find(self, data) -> int:
        a = self.head
        index = 0
        while a is not None:
            if a.data == data:
                return index
            a = a.next
            index += 1
        return -1

    #清空整个链表
    def clear(self):
        self.head = None
        self._length = 0

    #按顺序遍历链表，返回 Python 列表
    def to_list(self) -> list:
        a_list = []
        a = self.head
        while a is not None:
            a_list.append(a.data)
            a = a.next
        return a_list

    #链表反转（迭代法）
    def RevLinkedList(self):
        a = None
        b = self.head
        while b is not None:
            c = b.next
            b.next = a
            a = b
            b = c
        self.head = a

    #链表反转（递归）                          时间复杂度 O(n)，空间复杂度 O(n)，因为递归调用栈的深度是 n
    def reverse_recursive(self):
        def _reverse(node):
            if node is None or node.next is None:        #终止条件：空链表，或者只有一个节点，直接返回
                return node
            new_head = _reverse(node.next)               #递归反转 node 后面的链表
            node.next.next = node                        #让原来的下一个节点指回当前节点
            node.next = None                             #当前节点变成新链表的尾节点
            return new_head
        self.head = _reverse(self.head)

    #查找倒数第 k 个节点
    #让 fast 先走 k 步，然后 fast 和 slow 一起走，当 fast 走到 None 时，slow 正好在倒数第 k 个节点。
    def findKthFromEnd(self,k):
        if k <=0 or k > self._length:
            return None
        fast = slow = self.head
        for i in range(k):
            if fast is None:
                return None
            fast = fast.next
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow

    #查找链表中间节点,快的走俩，慢的一个一个走
    def MiddleLinkedList(self):
        if self.head is None:
            return None
        fast = slow = self.head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    #链表去重
    #版本1
    def RemoveDuplicatesList_banben1(self):
        a = self.head
        while a is not None:
            b  = a
            while b.next is not None:
                if b.next.data == a.data:
                    c = b.next
                    b.next = c.next
                    c.next = None
                    self._length -= 1
                else:
                    b = b.next
            a = a.next

    #版本2（有集合的）
    def RemoveDuplicatesList_banben2(self):
        a_set = set()
        a = None
        b = self.head
        while b is not None:
            if b.data in a_set:
                a.next = b.next
                b.next = None
                b = a.next
                self._length -= 1
            else:
                a_set.add(b.data)
                a = b
                b = b.next

#拓展部分1：哨兵
#我要用哨兵节点，是为了让头插、头删不再需要单独判断 head is None 或 index == 0，
# 所有插入删除统一为修改 prev.next
#它是不动的
class SentinelLinkedList:
    def __init__(self):
        self.head = LNode()
        self._length = 0

    def is_empty(self):
        return self.head.next is None

    def add_first(self, data):
        node = LNode(data)
        node.next = self.head.next
        self.head.next = node
        self._length += 1

    def add_last(self, data):
        c = self.head
        while c.next is not None:
            c = c.next
        c.next = LNode(data)
        self._length += 1

    def insert(self, index, data):
        if index < 0 or index > self._length:
            return False

        a = self.head
        for _ in range(index):
            a = a.next

        node = LNode(data)
        node.next = a.next
        a.next = node
        self._length += 1
        return True

    def remindex(self, index):
        if index < 0 or index >= self._length:
            return None

        a = self.head
        for _ in range(index):
            a = a.next

        b = a.next
        a.next = b.next
        b.next = None
        self._length -= 1
        return b.data

    def remoValue(self, data):
        a = self.head
        while a.next is not None:
            if a.next.data == data:
                b = a.next
                a.next = b.next
                b.next = None
                self._length -= 1
                return True
            a = a.next
        return False

    def list(self):
        result = []
        c = self.head.next
        while c is not None:
            result.append(c.data)
            c = c.next
        return result
#www.totuma.cn这个网站有不错的可视化，最开始学数据结构就用的这个