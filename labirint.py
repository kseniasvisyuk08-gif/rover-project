from random import *
labirint=[["." for x in range(8)] for y in range(8)]
labirint[2][1]="m"
labirint[0][5]='p'
labirint[5][3]="l"
labirint[6][0]='s'
labirint[2][5]="k"
labirint[7][4]="k"
labirint[5][3]="k"
labirint[7][7]='e'
labirint[0][7]='z'
labirint[1][2]="m"
labirint[4][4]="m"
labirint[7][2]='l'

labirint_p=[["." for x in range(8)] for y in range(8)]

def step1(step,tx,ty):
    if step == "up":
        tx -= 1
    elif step == "down":
        tx += 1
    if step == "left":
        ty -= 1
    elif step == "right":
        ty += 1
    return tx,ty
tx,ty=0,0
exit=0
sword=0
life=3
key=0
prz="*"
px,py=0,0
while exit==0:
    if life>0:
        print("твои жизни: ",life)
        labirint_p[px][py]=prz
        px,py=tx,ty
        prz=labirint_p[tx][ty]
        labirint_p[tx][ty]="Я"
        for x in labirint_p:
            print(*x)
        kolvosteps=randint(1,6)
        print("количество шагов: ",kolvosteps)
        for i in range(kolvosteps):
            step=str(input("up, down, left, right: "))
            tx,ty=step1(step,tx,ty)
            if tx<0 :
                print("ход сделать нельзя-стена")
                tx=0
                step = str(input("up, down, left, right: "))
                tx, ty = step1(step, tx, ty)
            if tx>7 :
                print("ход сделать нельзя-стена")
                tx=7
                step = str(input("up, down, left, right: "))
                tx, ty = step1(step, tx, ty)
            if ty<0 :
                print("ход сделать нельзя-стена")
                ty=0
                step = str(input("up, down, left, right: "))
                tx, ty = step1(step, tx, ty)
            if ty>7 :
                print("ход сделать нельзя-стена")
                ty=7
                step = str(input("up, down, left, right: "))
                tx, ty = step1(step, tx, ty)
        if labirint[tx][ty]=="m":
            print("Ты попал к монстру!!!")
            if sword==0:
                life-=1
                print("Тебе нужен меч")
                labirint_p[tx][ty]="m"
                tx,ty=0,0
            else:
                print("Монстр умер")
                labirint_p[tx][ty] = "m"
        elif labirint[tx][ty]=="l":
            print("Ты попал в ловушку")
            life-=1
            labirint_p[tx][ty]="l"
            tx, ty = 0, 0
        elif labirint[tx][ty]=="s":
            print("Ты нашел сундук с мечом")
            sword+=1
            labirint_p[6][0]="s"
        elif labirint[tx][ty]=='k':
            key+=1
            print("Ты нашел ключ от лабиринта!")
            labirint_p[tx][ty]='k'
        elif labirint[tx][ty]=='z':
            print("Ты нашел зелье жизни")
            life+=1
            labirint_p[tx][ty]='z'
        elif labirint[tx][ty]=='e':
            if key==0:
                print("Ты нашел выход, но не нашел ключ")
                life-=1
                labirint_p[7][7]='e'
                tx,ty=0,0
            else:
                print("Ты победил!")
                exit+=1
        elif labirint[tx][ty]=='p':
            labirint_p[tx][ty]='p'
            tx=randint(0,7)
            ty = randint(0, 7)
            if labirint[tx][ty] == "m":
                print("Ты попал к монстру!!!")
                if sword == 0:
                    life -= 1
                    print("Тебе нужен меч")
                    labirint_p[tx][ty] = "m"
                    tx, ty = 0, 0
                else:
                    print("Монстр умер")
                    labirint_p[tx][ty] = "m"
            elif labirint[tx][ty] == "l":
                print("Ты попал в ловушку")
                life -= 1
                labirint_p[tx][ty] = "l"
                tx,ty=0,0
            elif labirint[tx][ty] == "s":
                print("Ты нашел сундук с мечом")
                sword += 1
                labirint_p[6][0] = "s"
            elif labirint[tx][ty] == 'k':
                key += 1
                print("Ты нашел ключ от лабиринта!")
                labirint_p[tx][ty] = 'k'
            elif labirint[tx][ty] == 'z':
                print("Ты нашел зелье жизни")
                life += 1
                labirint_p[tx][ty] = 'z'
            elif labirint[tx][ty] == 'e':
                if key == 0:
                    print("Ты нашел выход, но не нашел ключ")
                    life -= 1
                    labirint_p[7][7] = 'e'
                    tx, ty = 0, 0
                else:
                    print("Ты победил!")
                    exit += 1
            else:
                labirint_p[tx][ty]="*"
        else:
            labirint_p[tx][ty]="*"

    else:
        exit+=1
        print("Ты проиграл")
