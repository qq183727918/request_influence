# _*_ coding: UTF-8 _*_
# @Time     : 2020/12/22 17:50
# @Author   : LiuXiaoQiang
# @Site     : https://github.com/qq183727918
# @File     : debugtest.py
# @Software : PyCharm

"""自动加双引号"""
with open('./test.txt', 'r')as f:
    a = f.readlines()
lists = []
for i in a:
    c = i.strip('\n')
    # print(c)
    lists.append(c)
lista = []
for i in lists:
    x = i.split(': ')
    # print(x)
    lista.append(x)
# print(lista)
lista1 = [['purchasePrice', 'null']]
listaa = []
for i in lista:
    ai = '"' + i[0] + '"' + ':'
    listaa.append(ai)
    if i[1] == 'null':
        ag = '"",' + '\n'
        listaa.append(ag)
    elif type(i[1]) == int or str:
        asd = i[1] + ',' + '\n'
        listaa.append(asd)
    else:
        print('不好意思，不认识这是什么')

print(listaa)
with open('./test_new.txt', 'w') as gs:
    gs.writelines(listaa)

