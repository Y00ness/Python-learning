#### Exercise 1

# Person_Info = input (' Please enter your name & your age seprated with a space:\n').split()
# Current_Year = 2024
# print (Person_Info , Current_Year + 100 - int(Person_Info[1]))

# #### Exercise 2
# Num = input('please add a num:\n')
# while True:
#     try:
#         Num = int(Num)
#         break
#     except:
#         Num=input('please enter a number: ')
# result = 'even' if Num%2==0 else 'odd'
# result = 'can be devided by 4' if Num%4==0 else result
# print (f'{Num} is {result}')


# #### Exercise 3
list_a=input('write numbers that seprated with space:\n').split()
print([int(x) for x in list_a if int(x)<10])