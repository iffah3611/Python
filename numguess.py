import random
print("welcome to the number guessing game")
print("as the game begins , lets give you a nickname :")
name = (input())
print("lets begin ,"+name)
print("i  will  think of a number and you will have to guess it")
print("you will have 10 attempts to guess ,if you fail your new nickname will be monkey")
while True:
    number = random.randint(1, 100)
    attempts = 10
    while attempts > 0:
        print("guess the number")
        guess = int(input())
        if guess == number:
            print("wow, "+name+" you guessed it right lets be friends")
            break
        elif guess < number:
            attempts -= 1
            print("your guess is too low,you have" +
                  str(attempts)+"attempts left")
        elif guess > number:
            attempts -= 1
            print("your guess is too high,you have" +
                  str(attempts)+"attempts left")
    if attempts == 0:
        print("you have exhausted all your attempts, your new nickname is monkey")
        print("the number was"+str(number))
    print("do you want to play again? (yes/no)")
    play_again = input().lower()
    if play_again == "yes" or play_again == "y":
        continue
    else:
        print("thanks for playing, see you next time!")
        break
