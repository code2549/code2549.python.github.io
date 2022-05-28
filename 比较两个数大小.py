# 比较两个数的最大值，（用户依次输入2个值，最后弹出最大的那个值）
num1 = int(input('请输入值1：'))
num2 = int(input('请输入值2：'))
if num1 > num2:
    print(f'最大值是{num1}')
elif num1 < num2:
    print(f'最大值是{num2}')
else:
    print('两个数都一样')
