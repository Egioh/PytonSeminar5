# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# оследний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint
def Game (turn, play1,play2,candy):
    if turn ==0:
        player1=play1
        player2=play2
    else:
        player1=play2
        player2=play1
    while candy>0:
        candy=candy-int(input(player1+"how many candy\'s you wish to take (from 1 to 28):"))
        print(f"candis={candy}")
        if candy<=0:
            print(player1+"winner")
            break
        candy=candy-int(input(player2+"how many candy\'s you wish to take (from 1 to 28):"))
        print(f"candis={candy}")
        if candy<=0:
            print(player2+"winner")
            break


def AiGame(turn, play1, play2, candy):
    aitake=0
    if turn ==0:
        player1=play1
        player2="Ai"
    else:
        player1="Ai"
        player2=play1
    if turn==0:
        print(f"first move to {player1}")
        while candy>0:
            candy=candy-int(input(player1+"how many candy\'s you wish to take (from 1 to 28):"))
            print(f"candis={candy}")
            if candy<=0:
                print(player1+" winner")
                break
        
            if candy>=56:
                aitake=28
                candy=candy-aitake
                print(f"AI take{aitake} candy\'s")
                print(f"candis={candy}")
            elif 29<candy<56:
                aitake=candy-29
                candy=candy-aitake
                print(f"AI take {aitake} candy\'s")
                print(f"candis={candy}")
            else:
                aitake=candy
                candy=candy-aitake
                print(f"AI take {aitake} candy\'s")
                print(f"candis={candy}")
            if candy<=0:
                print("AI winner, how predictable")
                break
    else:
        print(f"first move to {player1}")
        while candy>0:
            if candy>=56:
                aitake=28
                candy=candy-aitake
                print(f"AI take{aitake} candy\'s")
                print(f"candis={candy}")
            elif 29<candy<56:
                aitake=candy-29
                candy=candy-aitake
                print(f"AI take {aitake} candy\'s")
                print(f"candis={candy}")
            else:
                aitake=candy
                candy=candy-aitake
                print(f"AI take {aitake} candy\'s")
                print(f"candis={candy}")
            if candy<=0:
                print("AI winner, how predictable")
                break
            candy=candy-int(input(player1+"how many candy\'s you wish to take (from 1 to 28):"))
            print(f"candis={candy}")
            if candy<=0:
                print(player1+" winner")
                break



candy=100
player1=input("First player\'s name:")
gameType=int(input("input 0 if you want to play against undesputed AI or input 1 if against another miserable human: "))
player2="a"
if gameType==1:
    player2=input("Second player\'s name:")
    turn= randint(0,1)
    if turn==0:
        print(f"first turn to {player1}")
    else:
        print(f"first turn to {player2}")
    Game (turn,player1,player2,candy)
else:
    turn= randint(0,1)
    AiGame(turn,player1,player2,candy)
