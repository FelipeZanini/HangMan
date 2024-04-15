import os
import random
from words import array_animals

def word_data():
    indice = random.randint(0, 86)
    english = array_animals[indice][0]
    portuguese = array_animals[indice][1]
    categorie = array_animals[indice][2]
    indice_categorie = array_animals[indice][3]

    #print("ejfnsdfdsfs", array_animals[0][1])

    return indice, english, portuguese, categorie, indice_categorie


#def add_statistics(indice):



def run():
    os.system('cls')

    word = word_data()

    #print("_____________________________\n")
    print("[PTBR]", word[2], "\n")
    print("[EN]: ")
    answer = input()

    os.system('cls')

    print("------------------------------")

    #print("[PTBR " + word[2] + "]")
    #print("[EN " + word[1] + "]")
    #print("[Type " + word[3] + "]")
    #print("\n[Answer " + answer + "]")

    if answer.lower() == word[1].lower():
        print("Correct       " +  word[1])
        print(word[3])
    else:
        print("Incorrect       " +  word[1])

    print("------------------------------")


    print("\nNext [any key] - Menu = [M]")
    next = input()

    if next == "m":
        os.system("cls")
        menu()
    elif next != "m":
        run()
    
    #menu()


def statistic():
    return print("----- MENU/Statistics [ not implemented yet ]")
    
def config():
    os.system("cls")
    print("----- MENU/Config [ not implemented yet ]")
    
def exit():
    os.system("cls")
    print("Nice job! see you later!")


def menu():
    print("[LAN] Learning Animal Names - [PTBR to EN]\n")
    print("[1] Start\n[2] Statistics\n[3] Config\n[9] Exit")
    array_op = ['1', '2', '3', '9']
    op = input()
    os.system("cls")
    if op in array_op:
        op = int(op)
        if op == 1:
            run()
        elif op == 2:
            statistic()
            menu()
        elif op == 3:
            config()
            menu()
        elif op == 9:
            exit()
    else:
        os.system('cls')
        print("Keryword ["+ op +"] not found!")
        menu()
        

def main():

    os.system('cls')
    menu()


main()