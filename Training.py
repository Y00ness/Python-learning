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
lis_a,lis_b,lis_similars = range(0,4),range(2,10),[]
for i in lis_a:
    if i in lis_b: lis_similars.append(i)
print (lis_similars) 
