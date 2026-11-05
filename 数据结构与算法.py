# def for_loop(n: int):
#     res = 0
#     for i in range(1, n+1):
#         res += i
#     return res

# if __name__ == '__main__':
#     n = 5
#     res = for_loop(n)
#     print(f"\nfor 循环的求和结果 res = {res}")



# def while_loop_ii(n: int) -> int:
#     """while 循环（两次更新）"""
#     res = 0
#     i = 1  # 初始化条件变量
#     # 循环求和 1, 4, 10, ...
#     while i <= n:
#         res += i
#         # 更新条件变量
#         i += 1
#         i *= 2
#     return res


# def nested_for_loop(n: int) -> str:
#     """双层 for 循环"""
#     res = ""
#     # 循环 i = 1, 2, ..., n-1, n
#     for i in range(1, n + 1):
#         # 循环 j = 1, 2, ..., n-1, n
#         for j in range(1, n + 1):
#             res += f"({i}, {j}), "
#     return res


# # 算法 A 的时间复杂度：常数阶
# def algorithm_A(n: int):
#     print(0)
# # 算法 B 的时间复杂度：线性阶
# def algorithm_B(n: int):
#     for _ in range(n):
#         print(0)
# # 算法 C 的时间复杂度：常数阶
# def algorithm_C(n: int):
#     for _ in range(1000000):
#         print(0)

# def constant(n: int) -> int:
#     """常数阶"""
#     count = 0
#     size = 100000
#     for _ in range(size):
#         count += 1
#     return count


# def constant(n: int) -> int:
# 	    """常数阶"""
# 	    count = 0
# 	    size = 10
# 	    for _ in range(size):
# 	        count += 1
# 	    return count
	
# """Driver Code"""
# if __name__ == "__main__":
# 	    n = 8
# 	    print("输入数据大小 n =", n)
	
# 	    count = constant(n)
# 	    print("常数阶的操作数量 =", count)



# def linear(n) -> int:
# 	    """线性阶"""
# 	    count = 0
# 	    for _ in range(n):
# 	        count += 1
# 	    return count
	
# """Driver Code"""	
# if __name__ == "__main__":
# 	    n = 8
# 	    print("输入数据大小 n =", n)
	
# 	    count = linear(n)
# 	    print("线性阶的操作数量 =", count)




# class Node:
#     """类"""
#     def __init__(self, x: int):
#         self.val: int = x              # 节点值
#         self.next: Node | None = None  # 指向下一节点的引用

# def function() -> int:
#     """函数"""
#     # 执行某些操作...
#     return 0

# def algorithm(n) -> int:  # 输入数据
#     A = 0                 # 暂存数据（常量，一般用大写字母表示）
#     b = 0                 # 暂存数据（变量）
#     node = Node(0)        # 暂存数据（对象）
#     c = function()        # 栈帧空间（调用函数）
#     return A + b + c      # 输出数据



# from curses import resize_term


# def sum_iter(n: int) -> int:
#     """迭代求和"""
#     res = 0
#     for i in range(1, 5):
#         res += i
#     return res
# print('res')
# # def sum_recur(n: int) -> int:
# #     """递归求和"""
# #     if n == 1:
# #         return 1
# #     return n + sum_recur(n - 1)



# class ListNode:
# 	    """链表节点类"""
# 	    def __init__(self, val: int):
# 	        self.val: int = val  # 节点值
# 	        self.next: ListNode | None = None  # 后继节点引用
	
# """Driver Code"""
# if __name__ == "__main__":
# 	    # 使用多种基本数据类型来初始化数组
# 	    numbers = [0] * 5
# 	    decimals = [0.0] * 5
# 	    # Python 的字符实际上是长度为 1 的字符串
# 	    characters = ['0'] * 5
# 	    bools = [False] * 5
# 	    # Python 的列表可以自由存储各种基本数据类型和对象引用
# 	    data = [0, 0.0, 'a', False, ListNode(0)]




# print(10 / 0)
# open('data.txt')
# open("C:/Windows/system32/hosts", "w")
# os = 1
# print(os.mkdir("新建文件夹"))
# open("D:/素材")
# import requests
# requests.get("http://10.255.255.1", timeout=1)

# import socket
# s = socket.create_connection(("127.0.0.1", 9999))

# from math import sqr
# import 不存在的库

# import pandas

# it = iter([1, 2])
# print(next(it), next(it))

# def f():
#     return f(5)
# id

# print(f(5))

# try:
#     risky()
# except Exception as e:
#     print("出错了：", e)


# import traceback

# def risky():
#     return 1 / 0

# try:
#     risky()
# except ZeroDivisionError as e:      # 具体错误优先
#     print("已知问题：", e)
# except Exception as e:              # 兜底在后
#     traceback.print_exc()           # 打印完整调用栈留证据
# finally:
#     print("无论成败都执行：清理资源")




# import warnings

# warnings.filterwarnings("自定义提醒")



# "你好".encode("ascii")
# # ← 中文超出 ASCII 范围，报 UnicodeEncodeError
# b"\xd6\xd0".decode("utf-8")   # ← 字节不是合法 UTF-8，报 UnicodeDecodeError


# raise ExceptionGroup("批量错误", [ValueError("a"), TypeError("b")])




# import sys
# sys.exit(1)








# arr: list[int] = [0] * 5  # [ 0, 0, 0, 0, 0 ]
# nums: list[int] = [1, 3, 2, 5, 4]
# print(arr)
# print(nums)

# def traverse(nums: list[int]):
#     """遍历数组"""
#     count = 0
#     # 通过索引遍历数组
#     for i in range(len(nums)):
#         count += nums[i]
#     # 直接遍历数组元素
#     for num in nums:
#         count += num
#     # 同时遍历数据索引和元素
#     for i, num in enumerate(nums):
#         count += nums[i]
#         count += num

# """Driver Code"""
# if __name__ == "__main__":
#        nums = ([1, 3, 2, 5, 4])
#        print("数组 nums =", nums)
#        traverse(nums)



# class ListNode:
# 	    """链表节点类"""
# 	    def __init__(self, val: int):
# 	            self.val: int = val  # 节点值
# 	            self.next: ListNode | None = None  # 后继节点引用
	
# """Driver Code"""
# if __name__ == "__main__":
# 	    # 初始化链表 1 -> 3 -> 2 -> 5 -> 4
# 	    # 初始化各个节点
# 	    n0 = ListNode(1)
# 	    n1 = ListNode(3)
# 	    n2 = ListNode(2)
# 	    n3 = ListNode(5)
# 	    n4 = ListNode(4)
# 	    # 构建节点之间的引用
# 	    n0.next = n1
# 	    n1.next = n2
# 	    n2.next = n3
# 	    n3.next = n4



# from collections import deque

# # 初始化双向队列
# deq: deque[int] = deque()

# # 元素入队
# deq.append(2)      # 添加至队尾
# deq.append(5)
# deq.append(4)
# deq.appendleft(3)  # 添加至队首
# deq.appendleft(1)

# # 访问元素
# front: int = deq[0]  # 队首元素
# rear: int = deq[-1]  # 队尾元素

# # 元素出队
# pop_front: int = deq.popleft()  # 队首元素出队
# pop_rear: int = deq.pop()       # 队尾元素出队

# # 获取双向队列的长度
# size: int = len(deq)

# # 判断双向队列是否为空
# is_empty: bool = len(deq) == 0




# class ListNode:
#     """双向链表节点"""

#     def __init__(self, val: int):
#         """构造方法"""
#         self.val: int = val
#         self.next: ListNode | None = None  # 后继节点引用
#         self.prev: ListNode | None = None  # 前驱节点引用

# class LinkedListDeque:
#     """基于双向链表实现的双向队列"""

#     def __init__(self):
#         """构造方法"""
#         self._front: ListNode | None = None  # 头节点 front
#         self._rear: ListNode | None = None  # 尾节点 rear
#         self._size: int = 0  # 双向队列的长度

#     def size(self) -> int:
#         """获取双向队列的长度"""
#         return self._size

#     def is_empty(self) -> bool:
#         """判断双向队列是否为空"""
#         return self._size == 0

#     def push(self, num: int, is_front: bool):
#         """入队操作"""
#         node = ListNode(num)
#         # 若链表为空，则令 front 和 rear 都指向 node
#         if self.is_empty():
#             self._front = self._rear = node
#         # 队首入队操作
#         elif is_front:
#             # 将 node 添加至链表头部
#             self._front.prev = node
#             node.next = self._front
#             self._front = node  # 更新头节点
#         # 队尾入队操作
#         else:
#             # 将 node 添加至链表尾部
#             self._rear.next = node
#             node.prev = self._rear
#             self._rear = node  # 更新尾节点
#         self._size += 1  # 更新队列长度

#     def push_first(self, num: int):
#         """队首入队"""
#         self.push(num, True)

#     def push_last(self, num: int):
#         """队尾入队"""
#         self.push(num, False)

#     def pop(self, is_front: bool) -> int:
#         """出队操作"""
#         if self.is_empty():
#             raise IndexError("双向队列为空")
#         # 队列长度为 1 时, 头尾指向同一节点
#         if self._size == 1:
#             val: int = self._front.val
#             self._front = None
#             self._rear = None
#         # 队首出队操作
#         elif is_front:
#             val: int = self._front.val  # 暂存头节点值
#             # 删除头节点
#             fnext: ListNode | None = self._front.next
#             fnext.prev = None
#             self._front.next = None
#             self._front = fnext  # 更新头节点
#         # 队尾出队操作
#         else:
#             val: int = self._rear.val  # 暂存尾节点值
#             # 删除尾节点
#             rprev: ListNode | None = self._rear.prev
#             rprev.next = None
#             self._rear.prev = None
#             self._rear = rprev  # 更新尾节点
#         self._size -= 1  # 更新队列长度
#         return val

#     def pop_first(self) -> int:
#         """队首出队"""
#         return self.pop(True)

#     def pop_last(self) -> int:
#         """队尾出队"""
#         return self.pop(False)

#     def peek_first(self) -> int:
#         """访问队首元素"""
#         if self.is_empty():
#             raise IndexError("双向队列为空")
#         return self._front.val

#     def peek_last(self) -> int:
#         """访问队尾元素"""
#         if self.is_empty():
#             raise IndexError("双向队列为空")
#         return self._rear.val

#     def to_array(self) -> list[int]:
#         """返回数组用于打印"""
#         node = self._front
#         res = [0] * self.size()
#         for i in range(self.size()):
#             res[i] = node.val
#             node = node.next
#         return res



# class HashMapChaining:
#     """链式地址哈希表"""

#     def __init__(self):
#         """构造方法"""
#         self.size = 0  # 键值对数量
#         self.capacity = 4  # 哈希表容量
#         self.load_thres = 2.0 / 3.0  # 触发扩容的负载因子阈值
#         self.extend_ratio = 2  # 扩容倍数
#         self.buckets = [[] for _ in range(self.capacity)]  # 桶数组

#     def hash_func(self, key: int) -> int:
#         """哈希函数"""
#         return key % self.capacity

#     def load_factor(self) -> float:
#         """负载因子"""
#         return self.size / self.capacity

#     def get(self, key: int) -> str | None:
#         """查询操作"""
#         index = self.hash_func(key)
#         bucket = self.buckets[index]
#         # 遍历桶，若找到 key ，则返回对应 val
#         for pair in bucket:
#             if pair.key == key:
#                 return pair.val
#         # 若未找到 key ，则返回 None
#         return None

#     def put(self, key: int, val: str):
#         """添加操作"""
#         # 当负载因子超过阈值时，执行扩容
#         if self.load_factor() > self.load_thres:
#             self.extend()
#         index = self.hash_func(key)
#         bucket = self.buckets[index]
#         # 遍历桶，若遇到指定 key ，则更新对应 val 并返回
#         for pair in bucket:
#             if pair.key == key:
#                 pair.val = val
#                 return
#         # 若无该 key ，则将键值对添加至尾部
#         pair = Pair(key, val)
#         bucket.append(pair)
#         self.size += 1

#     def remove(self, key: int):
#         """删除操作"""
#         index = self.hash_func(key)
#         bucket = self.buckets[index]
#         # 遍历桶，从中删除键值对
#         for pair in bucket:
#             if pair.key == key:
#                 bucket.remove(pair)
#                 self.size -= 1
#                 break

#     def extend(self):
#         """扩容哈希表"""
#         # 暂存原哈希表
#         buckets = self.buckets
#         # 初始化扩容后的新哈希表
#         self.capacity *= self.extend_ratio
#         self.buckets = [[] for _ in range(self.capacity)]
#         self.size = 0
#         # 将键值对从原哈希表搬运至新哈希表
#         for bucket in buckets:
#             for pair in bucket:
#                 self.put(pair.key, pair.val)

#     def print(self):
#         """打印哈希表"""
#         for bucket in self.buckets:
#             res = []
#             for pair in bucket:
#                 res.append(str(pair.key) + " -> " + pair.val)
#             print(res)

# """Driver Code"""
# if __name__ == "__main__":
# 	    hashmap = HashMapChaining()
	
	
# 	    hashmap.put(12836, "小哈")
# 	    hashmap.put(15937, "小啰")
# 	    hashmap.put(16750, "小算")
# 	    hashmap.put(13276, "小法")
# 	    hashmap.put(10583, "小鸭")
	
	
# 	    name = hashmap.get(13276)
	
	
# 	    hashmap.remove(12836)





# class TreeNode:
# 	    """二叉树节点类"""
# 	    def __init__(self, val: int):
# 	        self.val: int = val                # 节点值
# 	        self.left: TreeNode | None = None  # 左子节点引用
# 	        self.right: TreeNode | None = None # 右子节点引用
	
# """Driver Code"""
# if __name__ == "__main__":
# 	    # 初始化二叉树
# 	    # 初始化节点
# 	    n1 = TreeNode(val=1)
# 	    n2 = TreeNode(val=2)
# 	    n3 = TreeNode(val=3)
# 	    n4 = TreeNode(val=4)
# 	    n5 = TreeNode(val=5)
# 	    # 构建节点之间的引用（指针）
# 	    n1.left = n2
# 	    n1.right = n3
# 	    n2.left = n4
# 	    n2.right = n5





# form collection import deque

# class TreeNode:
#     """二叉树节点类"""
#     def __init__(self, val: int):
#         self.val: int = val
#         self.left: TreeNode | None = None
#         self.right: TreeNode | Noen = None

# def list_to_tree_dfs(arr: list[int], i: int) -> TreeNode | None:
#     if i < 0 or i >= len(arr) or arr[i] is None:
#         return None
#         root.left = list_to_tree_dfs(arr, 2 * i + 1)
#         root.right = list_to_tree_dfs(arr, 2 * i + 2)




# class TreeNode:
#     """AVL 树节点类"""
#     def __init__(self, val: int):
#         self.val: int = val
#         self.height: int = 0
#         self.left: TreeNode | None = None
#         self.right: TreeNode | None = None
        

# class MaxHeap:
#     """大顶堆"""

#     def __init__(self, nums: list[int]):
#         """构造方法"""
#         # 将列表元素原封不动添加进堆
#         self.max_heap = nums

#     def left(self, i: int) -> int:
#         """获取左子节点的索引"""
#         return 2 * i + 1

#     def right(self, i: int) -> int:
#         """获取右子节点的索引"""
#         return 2 * i + 2

#     def parent(self, i: int) -> int:
#         """获取父节点的索引"""
#         return (i - 1) // 2  # 向下整除

#     def size(self) -> int:
#         """获取堆大小"""
#         return len(self.max_heap)

#     def is_empty(self) -> bool:
#         """判断堆是否为空"""
#         return self.size() == 0

#     def peek(self) -> int:
#         """访问堆顶元素"""
#         return self.max_heap[0]


# """Driver Code"""
# if __name__ == "__main__":
#     # 初始化大顶堆
#     # 请注意，输入数组已经是一个已经是一个合法的堆 
#     max_heap = MaxHeap([9, 8, 6, 6, 7, 5, 2, 1, 4, 3, 6, 2])

#     # 获取堆顶元素
#     peek = max_heap.peek()
#     print(f"\n堆顶元素为 {peek}")



# class MaxHeap:
#     """大顶堆"""

#     def __init__(self, nums: list[int]):
#         """构造方法，根据输入列表建堆"""
#         # 将列表元素原封不动添加进堆
#         self.max_heap = nums
#         # 堆化除叶节点以外的其他所有节点
#         for i in range(self.parent(self.size() - 1), -1, -1):
#             self.sift_down(i)

#     def left(self, i: int) -> int:
#         """获取左子节点的索引"""
#         return 2 * i + 1

#     def right(self, i: int) -> int:
#         """获取右子节点的索引"""
#         return 2 * i + 2

#     def parent(self, i: int) -> int:
#         """获取父节点的索引"""
#         return (i - 1) // 2  # 向下整除

#     def swap(self, i: int, j: int):
#         """交换元素"""
#         self.max_heap[i], self.max_heap[j] = self.max_heap[j], self.max_heap[i]

#     def size(self) -> int:
#         """获取堆大小"""
#         return len(self.max_heap)

#     def sift_down(self, i: int):
#         """从节点 i 开始，从顶至底堆化"""
#         while True:
#             # 判断节点 i, l, r 中值最大的节点，记为 ma
#             l, r, ma = self.left(i), self.right(i), i
#             if l < self.size() and self.max_heap[l] > self.max_heap[ma]:
#                 ma = l
#             if r < self.size() and self.max_heap[r] > self.max_heap[ma]:
#                 ma = r
#             # 若节点 i 最大或索引 l, r 越界，则无须继续堆化，跳出
#             if ma == i:
#                 break
#             # 交换两节点
#             self.swap(i, ma)
#             # 循环向下堆化
#             i = ma


# """Driver Code"""
# if __name__ == "__main__":
#     # 初始化大顶堆
#     max_heap = MaxHeap([1, 2, 3, 4, 5])






