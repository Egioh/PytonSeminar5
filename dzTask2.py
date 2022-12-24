flag=True
def WinX(mas):
    count=0
    for i in range (3):
        if "O" not in mas[i] and "." not in mas[i]:
            return True
    for x in range (3):
        o=[mas[0][x],mas[1][x],mas[2][x]]
        if "O" not in o:
            return True
    


def WinO(mas):
    count=0
    for i in range (3):
        if "x" not in mas[i] and "." not in mas[i]:
            return True
    for x in range (3):
        o=[mas[0][x],mas[1][x],mas[2][x]]
        if "x" not in o:
            return True



mas = [[".", ".", "."], [".", ".", "."], [".", ".", "."]]
def printMas (mas):
    for i in range(0, len(mas)):
        for j in range(0, len(mas[i])):
            print(mas[i][j], end=' ')
        print()
printMas(mas)
def char_positionX (mas):
    x=int(input("куда ставим крестик (строка 1-3)"))-1
    y=int(input("куда ставим крестик (столбец 1-3)"))-1
    mas[x][y]= "x"
    printMas(mas)
def char_positionO (mas):
    x=int(input("куда ставим нолик (строка 1-3)"))-1
    y=int(input("куда ставим нолик (столбец 1-3)"))-1
    mas[x][y]= "O"
    printMas(mas)
while flag:
    char_positionX(mas)
    flag=WinX(mas)
   
    char_positionO(mas)
    flag=WinO(mas)
print("game over")
       
    


