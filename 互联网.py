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


# from urllib.request import urlopen
# with urlopen('https://docs.python.org/3/') as response:



# import socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_address = ('localhost', 1313)
# print('connecting to %s port %s' % server_address)
# sock.connect(server_address)
# massage = b'Tnfinity...'
#  print('Client sending "%s"' % message.decode())
# sock.sendall(massage)
# reply = sock.recv(11)
# print('Client received ' '%s' % reply.dacode())
# sock.close()



# import socket
#  # Create a TCP/IP socket 
#  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
#  # Connect to the server listening at localhost:1313 
#  server_address = ('localhost', 1313) 
#  print('Connecting to %s:%s' % server_address) 
#  sock.connect(server_address) 
#  # Send request message 
#  message = b'To Infinity...' 
#  print('Client sending "%s"' % message.decode()) 
#  sock.sendall(message) 
#  # Receive reply from server 
#  reply = sock.recv(11) 
#  print('Client received "%s"' % reply.decode()) 
#  # Close the server connection 
#  sock.close()


# from urllib.request import urlopen
# with urlopen('https://docs.python.org/3/') as response:
#     for line in response:
#         line = line.decode()
#         if 'updated' in line:
#             print(line.rstrip())


# import hashlib, hmac

# def sha(s):
#     return hashlib.sha256(s.encode()).hexdigest()

# print("1 确定性", sha("hello"))
# print("2 雪崩 ", sha("hello")[:8], "vs", sha("hello1")[:8])
# print("3 定长 ", len(sha("x" * 1_000_000)), "个节符")
# print("4 加盐 ", sha("salt-A:hello")[:16], sha("salt-B:hello")[:16])
# print("5 HMAC ", hmac.new(b'secret-key', b'hello', hashlib.sha256).hexdigest()[:16])




# class GradeBook:
#     def __init__(self, scores):
#         self.scores = scores
#         print("创建对象，self 收到：", scores)

#     def passed(self):
#         print("passed() 内部 self.scores =", self.scores)
#         return [s for s in self.scores if s >= 60]

#     def avg_passed(self):
#         p = self.passed()
#         return sum(p) / len(p) if p else 0

# book = GradeBook([78, 45, 90, 59, 66])
# print("及格：", book.passed())
# print("平均分：", book.avg_passed())
