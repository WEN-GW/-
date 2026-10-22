# num = float(input("请输入一个数："))
# if num > 0:
#     print("这是一个正数")
# elif num < 0:
#     print("这是一个负数")
# else:
#     print("这是一个零")


# score = float(input("请输入一个成绩："))
# if score >= 90:
#     print("优秀")
# elif score >= 80:
#     print("良好")
# elif score >= 70:
#     print("中等")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")




# num = int(input("输入一个大于1的整数"))

# if num <= 1:
#     print("输入大于1的整数")
# else:
#     is_prime = True
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{num}是质数")
#     else:
#         print(f"{num}不是质数")





# balance = 0
# while True:
#     print(f"当前余额为:{balance}元")
#     print("请选择操作：")
#     print("1.存钱")
#     print("2.取钱")
#     print("3.退出")
#     choice = input("请选择操作(1-3):")
#     if choice == "1":
#         # 存钱
#         amount = float(input("请输入存钱金额："))
#         if amount > 0:
#             balance += amount
#             print(f"存钱成功,存入{amount}元,当前余额为{balance}元")
#         else:
#             print("输入有误，请重新输入,存款金额必须大于0")
#     elif choice == "2":
#         # 取钱
#         amount = float(input("请输入取钱金额："))
#         if amount > 0:
#             if amount <= balance:
#                 balance -= amount
#                 print(f"取钱成功，取出{amount}元，当前余额为{balance}元")
#             else:
#                 print("余额不足")
#         else:        
#             print(f"取款金额必须大于0")
#     elif choice == "3":
#         # 退出
#         print("退出成功")
#         break
#     else:
#         print("无效选项")



# fruits = ["苹果", "香蕉", "橘子"]

# # 只取值(最常用)
# for f in fruits:
#     print(f)

# # 同时要下标和值 → enumerate
# for i, f in enumerate(fruits):
#     print(i, f)         # 0 苹果 / 1 香蕉 / 2 橘子



# duration = int(input("请输入停车时长（分钟）："))
# if duration >= 0 and duration <= 30:
#     print("停车20分钟,免费")
# else:
#     time = duration - 30
#     price = time * 0.5
#     print(f"停车{duration}分钟,收费{price:.2f}元")





