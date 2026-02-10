import random
#初始化抽奖池
DB_list=[]
#增加模块
def add_for_DB_list(quanzhong=1):
        name=input("输入你要增加的名字：")
        for i in range(quanzhong):
            DB_list.append(name)
#删除模块
def delete_for_DB_list():
    name = input('输入你要删除的名字:').strip()
    if name not in DB_list:
        print("名单里没有这个名字哦～")
        return
    count = 0
    while name in DB_list:
        DB_list.remove(name)
        count += 1
    print(f"已删除 {name} 的全部 {count} 条记录")
#抽奖模块
def choujiang(shuliang):
    huojiang=random.sample(DB_list,shuliang)
    print(huojiang)
while True:
    shijian=input("显示名单，增加，删除，开始，退出，请输入你要触发的事件：")
    if shijian=='增加':
        add_for_DB_list()
    elif shijian=='zj':
        quanzhong=int(input("请输入一个正整数增加权重："))
        add_for_DB_list(quanzhong)
    elif shijian=='删除':
            delete_for_DB_list()
    elif shijian=='退出':
        break
    elif shijian == '显示名单':
        print(DB_list)
    elif shijian == '开始':
        while True:
            try:
                shuliang = int(input("输入要抽取的人数："))
                choujiang(shuliang)
                break
            except ValueError:
                print("请输入正整数！")
            except Exception as e:
                print("出错了，请重试！")

    else:
        print("无效命令！请检查拼写～")
