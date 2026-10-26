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



