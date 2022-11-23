import math
import time


def weekday():
    day=int(input("введите число от 1 до 7 ->"))
    if (day == 7) or (day == 6):
        print("выходной")
    elif (day > 7) or (day < 1):
        print("введите число от 1 до 7")
    else: print("не выходной")

def boolean_test():
    "2-    Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \nдля всех значений предикат. ⋀ - and ⋁ - or ¬ - not\n"
    X = bool(input("введите значение 1 True  или  Fasle "))

    Y = bool(input("введите значение 2 True  или  Fasle "))
    Z = bool(input("введите значение 3 True  или  Fasle "))
    if  not(X or Y or Z) == ( (not X ) and (not Y) and (not Z) ):
        print("все верно\n "
              "not(X or Y or Z) == ( (not X ) and (not Y) and (not Z) ) ")
    else:
        print("что-то пошло не так")

def cvart_num():
    X=int(input("введите координату Х: "))
    Y=int(input("введите координату Y: "))
    if (Y==0):
        print("точка лежит на прямой Y/ шеф приказал исключить"
              "этот случай")
    elif (X==0):
        print("точка лежит на прямой X/ шеф приказал исключить"
              "этот случай")
    elif (X>0):
        if (Y>0):
            print("->1")
        else:
            print("->4")
    else :
        if (Y > 0):
            print("->2")
        else:
            print("->3")

def diapozon_coordinat():
    cvart_number=int(input("введите номер координатной четверти(1-4)"))
    if cvart_number == 1:
        print("X>0,Y>0")
    elif cvart_number ==2:
        print("X<0,Y>0")
    elif cvart_number ==3:
        print("X<0,Y<0")
    elif cvart_number ==4:
        print("X>0,Y<0")
    else: print("некорректный ввод данных")

def evclid_dist():
    Ax = float(input("введите координату X точки А "))
    Bx = float(input("введите координату X точки B "))
    Ay = float(input("введите координату Y точки А "))
    By = float(input("введите координату Y точки B "))
    distance=math.sqrt ((Ax-Bx)*(Ax-Bx)+(Ay-By)*(Ay-By))
    print(f"A({Ax},{Ay}); B({Bx};{By}) \n"
          f"расстояние в 2D -> {distance}")

def one_more():
    answer=input("нажмите любую клавишу для продолжения")
    main()


def main():
    check_task=int(input("какое задание проверить?\n"
                     "0-закрыть программу\n"
                         "1-    Напишите программу, которая принимает на вход цифру, обозначающую день недели,\n и проверяет, является ли этот день выходным.\n"
                     "2-    Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \nдля всех значений предикат. ⋀ - and ⋁ - or ¬ - not\n"
                        "3-    Напишите программу, которая принимает на вход координаты точки (X и Y),\n причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.)\n"
                         "4-    программу, которая по заданному номеру четверти, \nпоказывает диапазон возможных координат точек в этой четверти (x и y).\n"
                         "5-    Напишите программу, которая принимает на вход координаты двух точек \nи находит расстояние между ними в 2D пространстве.\n"
                         "\nномер задания: "))
    if check_task == 1:
        weekday()
        one_more()
    elif check_task == 2:
        boolean_test()
        one_more()
    elif check_task == 3:
        cvart_num()
        one_more()
    elif check_task == 4:
        diapozon_coordinat()
        one_more()
    elif check_task ==5:
        evclid_dist()
        one_more()
    elif check_task == 0:
        print("консоль закроется черезе 6.66 секунд")
        time.sleep(6.66)

    else:print("введи цифроу 0-5")



if __name__ == '__main__':
    main()