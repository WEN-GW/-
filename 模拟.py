# memory = [
#     0x1A0B,   # A0: 把内存 0B 的数(7)装进寄存器 A
#     0x1A0C,   # A2: 把内存 0C 的数(5)装进寄存器 A
#     0xCAA0,   # A4: (示例简化) ...
#     0xC000,   # A6: 停机
# ]
# # 更清晰的简化版：自制三指令模型
# mem = {0x00: 0x1107,   # LOAD R1, 7      —— 把 7 装进寄存器 1
#        0x02: 0x1205,   # LOAD R2, 5      —— 把 5 装进寄存器 2
#        0x04: 0x5312,   # ADD  R3 = R1+R2 —— 3+... 结果放 R3
#        0x06: 0xF000,   # HALT
#        0xFF: 0}        # 内存尾

# reg = [0]*16     # 16 个通用寄存器
# pc = 0x00        # 程序计数器
# ir = 0           # 指令寄存器
# steps = 0        # 统计机器周期数

# while True:
#     steps += 1
#     ir = mem[pc]                    # ① 取指：按 PC 取指令进 IR
#     pc += 2                         #    PC 自动 +2（本模型指令占 2 字节）
#     op = (ir >> 12) & 0xF           # ② 译码：拆操作码（前 4 位）
#     r1 = (ir >> 8) & 0xF            #   第一个操作数（寄存器号）
#     val = ir & 0xFF                 #   第二个操作数（数值/地址）
#     if op == 0x1:                   # ③ 执行：分派
#         reg[r1] = val               #   LOAD
#     elif op == 0x5:                 #   ADD：寄存器+寄存器
#         r2 = (ir >> 4) & 0xF
#         reg[r1] = reg[r2] + reg[ir & 0xF]
#     elif op == 0xF:
#         break                       #   HALT
# print("R1 =", reg[1], "| R3 =", reg[3])   # R1 = 7 | R3 = 12
# print("机器周期跑了", steps, "圈")        # 4 圈

# # 实验2：对照真实 Python——dis.dis 看到的字节码就是"Python 的 Vole 指令"
# import dis
# def add(a, b): return a + b
# dis.dis(add)    # LOAD_FAST / LOAD_FAST / BINARY_OP / RETURN_VALUE
#                 # 解释器里跑的也是一个"取指译码执行"循环，只是取的是字节码

# # 实验3：while 循环 = 改 PC 的现场证明
# # 上面的 while True 每圈回到开头——如果把它翻成机器码，
# # 就是一条"无条件跳转"把 PC 改回循环体首地址





import re 
text = "联系我: 13812345678, 备用号 15987654321"

phones = re.findall(r'1\d{10}', text)
print(phones)

is_phone = re.fullmatch(r'1\d{10}', '13812345678')
print(bool(is_phone))


# import re

# text = "联系我：13812345678，备用号 15987654321"

# # 提取：找出所有手机号
# phones = re.findall(r"1\d{10}", text)
# print(phones)  # ['13812345678', '15987654321']

# # 验证：整个字符串是不是合法手机号
# is_phone = re.fullmatch(r"1\d{10}", "13812345678")
# print(bool(is_phone))  # True
