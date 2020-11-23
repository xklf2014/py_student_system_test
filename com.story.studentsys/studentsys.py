import os

file_name = 'student.txt'


def main_menu():
    print('-----------------------学生信息管理系统------------------------------')
    print('---------------------------功能菜单---------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出')
    print('--------------------------------------------------------------------')


def mian():
    while True:
        main_menu()
        chose = int(input('请选择'))
        if chose in [0, 1, 2, 3, 4, 5, 6, 7]:
            if chose == 0:
                answer = input('您确定退出系统吗？y/n').upper()
                if answer == 'Y':
                    print('谢谢使用')
                    break
                else:
                    continue
            elif chose == 1:
                insert()
            elif chose == 2:
                search()
            elif chose == 3:
                delete()
            elif chose == 4:
                update()
            elif chose == 5:
                sort()
            elif chose == 6:
                count()
            elif chose == 7:
                total()
        else:
            print('请选择0-7之间的数字')
            continue


def insert():
    stu_list = []
    while True:
        id = input('请输入学号(例1001):')
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩'))
            java = int(input('请输入java成绩'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue

        # 将录入的信息保存到学生字典中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生信息添加到学生列表中
        stu_list.append(student)

        answer = input('是否继续添加y/n:\n').upper()
        if answer == 'Y':
            continue
        else:
            break

    save(stu_list)
    print('学生信息录入完成!!!')


def search():
    stu_list = []
    while True:
        id = ''
        name = ''
        if os.path.exists(file_name):
            model = input('按ID查找请按1，按姓名查找请按2')
            if model == '1':
                id = input('请输入学生学号')
            elif model == '2':
                name = input('请输入学生姓名')
            else:
                print('输入错误请重新输入！！！')
                continue

            with open(file_name, 'r', encoding='utf-8') as rfile:
                students = rfile.readlines()
                for item in students:
                    stu = dict(eval(item))

                    if id != '':
                        if stu['id'] == id:
                            stu_list.append(stu)
                    elif name != '':
                        if stu['name'] == name:
                            stu_list.append(stu)
            # 显示查询结果
            show(stu_list)
            break
        else:
            print('尚未保存学生信息')
            return

    # 结果显示完成后需要清空列表
    stu_list.clear()
    isContinue = input('是否继续查询学生信息y/n').upper()
    if isContinue == 'Y':
        search()
    else:
        return


def delete():
    while True:
        id = input('请输入您要删除的学生学号')
        if not id:
            break

        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                student_old = file.readlines()
        else:
            student_old = []
        if student_old.__len__() != 0:
            flag = False  # 删除标记，false为未删除，true为已删除
            stu_dict = {}
            with open(file_name, 'w', encoding='utf-8') as wfile:
                for item in student_old:
                    stu_dict = dict(eval(item))  # 将字符串转换为字典
                    if stu_dict['id'] != id:
                        wfile.write(str(stu_dict) + '\n')
                    else:
                        flag = True

                    if flag:
                        print(f'id为{id}的学生信息已被删除')
                        break
                    else:
                        print(f'没有找到ID为{id}的学生信息')
                        break
        else:
            print('无学生信息，请确认!!!')
            break

    show()
    isContinue = input('是否继续删除学生信息y/n').upper()
    if isContinue == 'Y':
        delete()
    else:
        return


def update():
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
            stu_id = input('请输入您要修改的学生学号:')
            if not stu_id:
                return
            else:
                with open(file_name, 'w', encoding='utf-8') as wfile:
                    for item in student_old:
                        stu = dict(eval(item))
                        if stu['id'] == stu_id:
                            print('找到需要修改的学生信息:')
                            while True:
                                try:
                                    stu['name'] = input('请输入学生姓名')
                                    stu['english'] = int(input('请输入英语成绩:'))
                                    stu['python'] = int(input('请输入python成绩'))
                                    stu['java'] = int(input('请输入java成绩'))
                                except:
                                    print('输入信息有误，请重新输入')
                                wfile.write(str(stu) + '\n')
                                print('修改成功')
                                break
                        else:
                            wfile.write(stu + '\n')
            isContinue = input('是否继续修改学生信息y/n').upper()
            if isContinue == 'Y':
                update()
            else:
                return
    else:
        return


def sort():
    total()

    if os.path.exists(file_name):
        with open(file_name,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()

        stu_list=[]
        for item in students:
            stu=dict(eval(item))
            stu_list.append(stu)

        asc_or_desc_bool = False #排序初始化
        asc_or_desc=input('请选择(0为升序，1为降序')
        while True:
            if asc_or_desc == '0':

                break
            elif asc_or_desc == '1':
                asc_or_desc_bool = True
                break
            else:
                print('请输入0或者1')

        model=input('请选择排序方式(1.按照英语成绩排序 2.按照python成绩排序 3.按照java成绩排序 0.按照总成绩排序):')
        while True:
            if model == '1':
                stu_list.sort(key=lambda x:int(x['english']),reverse=asc_or_desc_bool)
                break
            elif model =='2':
                stu_list.sort(key=lambda x:int(x['python']),reverse=asc_or_desc_bool)
                break
            elif model == '3':
                stu_list.sort(key=lambda x:int(x['java']),reverse=asc_or_desc_bool)
                break
            elif model == '0':
                stu_list.sort(key=lambda x: int(x['english'])+int(x['python'])+int(x['java']), reverse=asc_or_desc_bool)
                break
            else:
                print('您输入的内容有误，请重新输入')

        #显示排序后的结果
        show(stu_list)


    else:
        return


def count():
    if os.path.exists(file_name):
        with open(file_name,'r',encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共存在{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print("系统暂未存在该数据")


def total():
    stu_list=[]
    if os.path.exists(file_name):
        with open(file_name,'r',encoding='utf-8') as rfile:
            students=rfile.readlines()
            if students:
                for item in students:
                    stu=dict(eval(item))
                    stu_list.append(stu)

                show(stu_list)
            else:
                print('学生信息为空')
                return
    else:
        print('暂未保存学生信息')


# 保存学生列表
def save(stu_list):
    try:
        with open(file_name, 'a', encoding='utf-8') as file:
            for item in stu_list:
                file.write(str(item) + '\n')
    except:
        print('保存失败')


def show(list):
    if len(list) == 0:
        print('没有查询到学生信息')
        return

    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'python成绩', 'java成绩', '总成绩'))
    format_data = '{:^7}\t{:^12}\t{:^8}\t{:^10}\t{:^14}\t{:^16}'
    for item in list:
        print(format_data.format(item.get('id'), item.get('name'), item.get('english'),
                                 item.get('python'), item.get('java'),
                                 int(item.get('english'))+ int(item.get('python'))+ int(item.get('java'))))


if __name__ == '__main__':
    mian()
