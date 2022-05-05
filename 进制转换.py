# 其他进制转十进制
# 二进制转十进制
two = input('请输入您要转为十进制的数字')
print(int(two, 2))

# 八进制转十进制
eight = input('请输入您要转换为十进制的数字')
print(int(eight, 8))

# 十六进制转十进制
sixteen = input('请输入您要转换为十进制的数字')
print(int(sixteen, 16))

# 十进制转其他进制
# 十进制转十六进制
tentosixteen = input('请输入您要转换为十六进制的数字')
print(hex(tentosixteen))

# 十进制转换为二进制
tentotwo = input('请输入您要转换为二进制的数字')
print(bin(tentotwo))

# 十进制转八进制
tentoeight = input('请输入您要转换为八进制的数字')
print(oct(tentoeight))


# 任意进制转换
snum = input('请选择要转换的进制数\n 1.二进制\n 2.十进制\n 3.八进制\n 4.十六进制')
if snum == '1':
    num2 = input('请输入一个二进制数字')
if snum == '2':
    num10 = input('请输入一个十进制数字')
if snum == '3':
    num8 = input('请输入一个八进制数字')
if snum == '4':
    num16 = input('请输入一个十六进制的数字')
