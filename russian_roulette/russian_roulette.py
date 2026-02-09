import random
import math
#随机选择一个弹仓
list=[1,2,3,4,5,6]
suiji_qiang=random.choice(list)
#塞入子弹
list_user=[1,2,3,4,5,6]
suiji_user=random.choice(list_user)
manye = 1
while True:
    yes_no = input('输入是开枪（yes/no）：')
    if suiji_user!=suiji_qiang and yes_no=="yes" :
        # 设置奖金
        manye += 1
        manye_manye=str(pow(10,manye))
        if suiji_user==6:
                suiji_user=1
        else:
                suiji_user+=1
        print(suiji_qiang)
        print(suiji_user)
    elif yes_no=="no":
        print('游戏结束，恭喜你还活着'+"，获得了"+manye_manye+'元')
        break
    else:
        manye=0
        manye_manye=str(0)
        print("你死了"+"获得"+manye_manye+'元')
        break
