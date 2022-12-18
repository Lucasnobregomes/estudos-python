#Guess the Number!
import random 


def main():

    print("hello player! what's your name?")
    my_name = input("write your name.")

    print("nice to meet you, " + my_name + ".")
    numero_da_máquina = random.randint(1,100)
    numero_da_máquina = int(numero_da_máquina)

    print("i'm thinking in a number. do you think you can guess it?")
    aceitação = input("tell me your wish.")

    if aceitação == "yes":
        print("ok! choose a number between 0 and 100.")
    elif aceitação == "no":
        print("i get it. goodbye.")
        return None
    else: 
        print("your inteligence is simple too small to contemplate this. goodbye mortal.")
        return None
  
    for numero_do_player in range(4):
        numero_do_player = input("your guess")
        numero_do_player = int(numero_do_player) #inverter 25-26 faz com que o numero do player da linha 27 seja uma string.

        if numero_do_player < numero_da_máquina:
            print("wrong guess! your guess is smaller than my number. take another one.")
        elif numero_do_player > numero_da_máquina:
            print("wrong guess! your guess is bigger than my number. take another one.")
        elif numero_do_player == numero_da_máquina:
            break

    if numero_do_player == numero_da_máquina:
        print("congratulations, you're a good opponent. you've guessed it in ")
    if numero_do_player != numero_da_máquina:
        print("you're weak. the chosen number is " + str(numero_da_máquina) + ".")


# Quando o arquivo executado for esse, ele vai chamar a funcao main
if __name__ == "__main__":
    main()
    