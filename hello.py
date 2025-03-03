print("Hello, World!")
print("My favourite colour is purple.")

name = input('Whats your name?: ') #This code asks for the users name
print(f'Greetings {name} ')

age = int(input('How old are you?: ')) #This code asks for the users age and prints both name and age    
print(f'{name}, Your {age}? You are very old')

if age > 25:
    print("Wow you are very old")

if age >= 13 and age <=19:
     print("You are a teenager like me!!")