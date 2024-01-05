#### Exercise 1

# Person_Info = input (' Please enter your name & your age seprated with a space:\n').split()
# Current_Year = 2024
# print (Person_Info , Current_Year + 100 - int(Person_Info[1]))

#### Exercise 2
Num = input('please add a num:\n')
while True:
    try:
        Num = int(Num)
        break
    except:
        Num=input('please enter a number: ')
odd_even = 'even' if Num%2==0 else 'odd'
print (f'{Num} is {odd_even}')