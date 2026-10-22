# def create_counter():
#     count = 0

#     def counter():
#         nonlocal count
#         count += 1
#         return count

#     return counter

# my_counter = create_counter()

# print(my_counter())  # 1
# print(my_counter())  # 2
# print(my_counter())  # 3



# def create_cached_calculator():
#     cache = {}
    
#     def calculate(x):
#         if x not in cache:
#             result = x * x * 2 * x + 1
#             cache[x] = result
#             print(f"计算{x}的结果为{result}")
#         else:
#             print(f"从缓存中获取{x}的结果为{cache[x]}")
#         return cache[x]

#     return calculate
# calculator = create_cached_calculator()

# calculator(2)  # 计算结果为17，并缓存
# calculator(3)  # 从缓存中获取结果为17
# calculator(2)  # 计算结果为54，并缓存
# calculator(3)  # 从缓存中获取结果为54





