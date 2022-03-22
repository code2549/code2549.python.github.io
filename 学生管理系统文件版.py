import os
stu_list = []


# 系统主界面函数
def show_menu():
    print('欢迎使用学生管理系统')
    print('1.添加学生')
    print('2.删除学生')
    print('3.修改学生信息')
    print('4.查询单个学生信息')
    print('5.查询所有的学生信息')
    print('6.退出系统')


# 添加学生信息函数
def insert_student():
    name = input('请输入学生名字：')
    for stu in stu_list:
        if stu['name'] == name:
            print('----------学生信息已存在！----------')
            return
    age = input('请输入学生年龄：')
    gender = input('请输入学生性别：')
    stu_dict = {'name': name, 'age': int(age), 'gender': gender}
    stu_list.append(stu_dict)
    print('----------学生信息添加成功！----------')


# 删除学生信息函数
def remove_student():
    name = input('请输入要删除的学生名字：')
    for stu in stu_list:
        if stu['name'] == name:
            stu_list.remove(stu)
            print('删除学生信息成功！')
            break
        else:
            print('----------该学生信息不存在！----------')


# 修改学生信息函数
def modify_student():
    name = input('请输入要修改的学生名字：')
    for stu in stu_list:
        if stu['name'] == name:
            stu['age'] = int(input('请输入新的年龄：'))
            stu['gender'] = input('请输入新的性别：')
            print('学生信息修改成功！')
            break
    else:
        print('----------该学生信息不存在！----------')


# 单个查询学生信息函数
def search_student():
    name = input('请输入要查询的学生名字：')
    for stu in stu_list:
        if stu['name'] == name:
            print(f'姓名:{stu["name"]}，年龄:{stu["age"]}，性别:{stu["gender"]}')
            break
    else:
        print('----------该学生信息不存在！----------')


# 查询所有学生信息函数
def show_all_info():
    if len(stu_list) > 0:
        for stu in stu_list:
            print(f'姓名:{stu["name"]}，年龄:{stu["age"]}，性别:{stu["gender"]}')
    else:
        print('目前没有学生信息')


def save():
    f = open('student.txt', 'w', encoding='utf-8')
    f.write(str(stu_list))
    f.close()


def load_file():
    global stu_list
    if os.path.exists('student.txt'):
        f = open('student.txt', 'r', encoding='utf-8')
        buf = f.read()
        if buf:
            stu_list = eval(buf)
        f.close()


# 无限循环，控制功能响应跳转
def main():
    load_file()
    while True:
        show_menu()
        opt = input('请输入用来选择的操作编号：')
        # 如果用户输入1，则调用添加学生信息函数
        if opt == '1':
            insert_student()
        # 如果用户输入2，则调用删除学生信息函数
        elif opt == '2':
            remove_student()
        # 如果用户输入3，则调用修改学生信息函数
        elif opt == '3':
            modify_student()
        # 如果用户输入4，则调用单个查询学生信息函数
        elif opt == '4':
            search_student()
        # 如果用户输入5，则调用查询所有学生信息函数
        elif opt == '5':
            show_all_info()
        # 如果用户输入6，直接终止循环执行，退出系统
        elif opt == '6':
            print('欢迎下次使用本系统')
            save()
            break
        # 如果用户输入了其他不合规定的，则提示输入有误，并重新进行循环
        else:
            print('输入有误，请再次输入')
            continue

        input('----------按回车键（enter）继续操作----------')


main()
