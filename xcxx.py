
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