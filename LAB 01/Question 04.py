#Write a Python program using a while loop that shows the following menu repeatedly until the
#user exits:
#1. Add two numbers
#2. Subtract two numbers
#3. Exit
def addtwo():
    n1 = int(input('Enter First Number: '))
    n2 = int(input('Enter Second Number: '))
    total = n1 + n2   
    print("Sum =", total)

def subtwo():
    n1 = int(input('Enter First Number: '))
    n2 = int(input('Enter Second Number: '))
    diff = n1 - n2
    print("Difference =", diff)

choice = 0

while (choice != 3):
    print('1. Add Two Numbers')
    print('2. Subtract Two Numbers')
    print('3. Exit')

    choice = int(input('Enter Your Choice: '))

    if choice == 1:
        addtwo()
    elif choice == 2:
        subtwo()
    elif choice == 3:
        break
