import random as ra

User = 1
Computer = 1
user_input2 = input("Enter either Odd or Even: ")
user_input1 = int(input("Enter a number between 1 and 6: "))
computer_input = ra.randint(1, 6)   
print("Computer choosen: ", computer_input)

the_toss = user_input1 + computer_input
if the_toss % 2 == 0:
    if user_input2 == "Even":
            input1 = input("User won..!! \n Enter Bat or Ball: ")
    else:
        if computer_input == "Even":
            input1 =  ra.choice(["Bat", "Ball"])
            print("You choosen to ", input1)
else:
    if user_input2 == "Odd":
            input1 = input("User won..!! \n Enter Bat or Ball: ")
    else:
        if computer_input == "Odd":
            input1 =  ra.choice(["Bat", "Ball"])
            print("You choosen to ", input1)

    print("You choosen to ", input1)

while user_input1 != computer_input:
    if (input1 == "Bat"):
        print("You Choosen to ", input1)
        print(User ,"rd ball")
        User +=1

    else:
        print("Computer choosen to ", input1)
        print("Computer ", Computer ,"rd ball")
        Computer += 1

print("Out..!")