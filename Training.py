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
# list_a=input('write numbers that seprated with space:\n').split()
# print([int(x) for x in list_a if int(x)<10])

# #### Exercise 4 - Divisors
# num,divisor_list=int(input('Please enter a number:\n')),[]
# for i in range(1,(num//2)+1):
#     if num%i==0: divisor_list.append(i)
# divisor_list.append(num)
# print(divisor_list)

# #### Exercise 5 
# lis_a,lis_b,lis_similars = range(0,4),range(2,10),[]
# for i in lis_a:
#     if i in lis_b: lis_similars.append(i)
# print (lis_similars) 

# #### Exercise 6
# var_str,polindrome=list(input('please write a word:\n')),0
# for i in range(0,len(var_str)):
#     if var_str[i] != var_str[-(i+1)]:
#         print("It's NOT a PALINDROME word")
#         polindrome=1
#         break
# if polindrome==0: print("It's a POLINDROME word")

# x= input('a word:\n')
# print('PLINDROME') if x==x[::-1] else print('NOT POLYNDRONE')

# #### Exercise 7
# a_list=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# even_numbers=[i for i in a_list if i%2==0]
# print(even_numbers)

# #### Exercise 8
# conditions=[['r','s'],['p','r'],['s','p']]
# while True:
#     player_a,player_b=input('Player 1: please choose R for rock,P for paper,os S for scissors ').lower(),input('Player 2: please choose R for rock,P for paper,os S for scissors ').lower()
#     var_x=[player_a,player_b]
#     if var_x in conditions: print('player 1 win!')
#     elif var_x[::-1] in conditions: print('player 2 win!')
#     else: print('draw!')
#     if input('Wanna play again?\n(press yes/no and enter)').lower()== 'no':break

# #### Exercise 9
# import random

# var_random=random.randint(1,9)
# while True:
#     guess_num=int(input('Please guess the number between 0 to 10: '))
#     if guess_num<var_random: print('too low! try again.', end=' ')
#     elif guess_num>var_random: print('too high! try again.', end=' ')
#     else:
#         print('Exactly right!')
#         break

# #### Exercise 10
# import random

# first_list=random.sample(range(20),10)
# second_list=random.sample(range(20),15)
# print(first_list,second_list)
# res_list=[i for i in first_list if i in second_list]
# print(res_list)

# #### Exercise 11
