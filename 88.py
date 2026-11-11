# ws["A1"] = "商品"             # 用坐标写入单元格
# ws["B1"] = "单价"
# ws["A2"] = "苹果"
# ws["B2"] = 5.8

# ws.append(["香蕉", 3.2])      # append 按行追加，自动写到第 3 行

# wb.save("测试.xlsx")          # 必须调用 save 才真正写进文件

# # ---------- 2. 读取 ----------
# wb2 = load_workbook("测试.xlsx")      # 打开已有文件
# ws2 = wb2["销售表"]                    # 按表名取工作表

# print(ws2["B2"].value)                # 输出: 5.8（记得加 .value）
# print(ws2.cell(row=3, column=2).value) # 数字坐标方式，输出: 3.2

# # 遍历整个表
# for row in ws2.iter_rows(values_only=True):
#     print(row)                        # 每次输出一行元组，如 ('商品', '单价')






# def spam(number1, number2):
#     return number1 / (number2 - 42)

# spam(101, 42)

# Traceback (most recent call last):
#   File "zeroDivideTraceback.py", line 4, in <module>
#     spam(101, 42)
#   File "zeroDivideTraceback.py", line 2, in spam
#     return number1 / (number2 - 42)
# ZeroDivisionError: division by zero
