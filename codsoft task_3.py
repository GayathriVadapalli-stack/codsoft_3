#Password Generator
import random       #importing random module

def generate_password():                           # defining password generator function
    print("WELCOME TO THE PASSWORD GENERATOR")
    
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'        #defining variables and assgining characters as strings
    special_characters = '!@#$%^&*()~?,.;{}[]\\|/+_=<>'
    numbers = '1234567890'
    
    num_letters = int(input("The number of letters you want: "))
    num_special_characters = int(input("The num of special characters you want: "))
    num_numbers = int(input("Enter the number of numbers you want: "))
    type_of_password = input("Type of password you want type 'easy' or 'hard': ").lower()
    #generating password using random module
    password_1 = random.choices(letters, k=num_letters) + random.choices(special_characters, k=num_special_characters) + random.choices(numbers, k =num_numbers)

    #Generating hard or easy password according to the user's choice
    if type_of_password == 'hard':
        random.shuffle(password_1)
        password = ''.join(password_1)  #joining the password into a string
        print(f'Your password is {password}')     #printing the generated password
    elif type_of_password == 'easy':
        password = ''.join(password_1)  #joining the password into a string
        print(f'Your password is {password}')     #printing the generated password
    else:
        print("Invalid Input.Try again!!")
    
    print("THANK YOU")

generate_password()