# 第一种方法，添加一个第三个容器，用于接收ap1和ap2的值。实现数据交换
apple1 = '青苹果'
apple2 = '红苹果'

apple3 = apple1
apple1 = apple2
apple2 = apple3
print(apple1)
print(apple2)

# 第二种方法，不添加任何的第三个容器，直接让左边等于右边，实现数据交换
banana1 = '黄香蕉'
banana2 = '白香蕉'
banana1, banana2 = banana2, banana1
print(banana1)
print(banana2)
