import random


def szam():
    szamai = random.randint(1, 50)
    print("I\A:")
    print("\t A generált szam: ",szamai)
    print("I\B:")
    if szamai % 5 == 0 and szamai % 3 == 0:
        print("\t A szám öttel és hárommal is osztható")
    elif szamai % 5 == 0:
        print("\t A szám öttel osztható")
    elif szamai % 3 == 0:
        print("\t A szám hárommal osztható")
    else:
        print()
