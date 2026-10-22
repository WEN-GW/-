# max = 10
# min = 5
# if max > min:
#     print("max > min")
# if max < min:
#     print("max < min")

# print("end")


# score = int(input("请输入成绩："))
# if score >= 60:
#     print("及格")
# else:
#     print("不及格")







# score = int(input("请输入考试成绩："))

# if score > 0 and score < 60:
#     print("不及格")
# elif score >= 60 and score < 80:
#     print("及格")
# elif score >= 80 and score < 90:
#     print("良好")
# elif score >= 90 and score < 100:
#     print("优秀")
# else:
#     print("输入错误")




age = int(input("请输入你的年龄："))
is_weekend = input("今天是不是周末(y/n:").lower()
price = 0
if age < 12:
    if is_weekend == 'y':
        price = 25
        print("儿童票：", price)
    else:
        price = 20
else:
    if is_weekend == 'y':    
        price = 40
        print("儿童票：", price)
    else:
        price = 50
print("票价：", price)