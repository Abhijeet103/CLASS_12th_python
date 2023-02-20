# # basic intro to what python is 
# #  output  , variables(rules for making variable) and input 
# # datatypes 
# # typeCasting 
# # Arithmetic operators 
# # logical operators 
# # flow of control ,  control statements : if else statement (taking decisions )
# # loops: while loop and For loop 
# # break and continue 


# #input --->  data ---> operation - > output

# print("5"+"9")
# var = 5 
# a = 9
# b =0
# # start with letters
# # dont use keywords 

# # a = input()
# # print(a)


# a = 7 # int 
# b = 3.6 # float 
# c = True # bool 
# d = "Abhijeet" # string 
# e ='4'

# #Arithmetic operators 
# # + , - , * ,  / ,  // floor division  , % modulus reminder  , ** power 


# a = 2 
# b = 3



# print(a/b)
# print(a//b)
# print(a**b)
# print(a%b)

# a = True 
# b = False

# c= a and b
# d = a or b 

# print(d)

# # comparision  > < >= <= , ==
# # = assingment operator 

# a = 7 
# b =8

# c = a <= b

# print(c)

# # if else  
# #65 drive with precaution 

# age  = 67

# if age>=65  :
#     print("drive with precaution ")
# elif age>=18 :
#     print("you can drive")
# elif age>=16 :
#     print("you can drive scooty")
# else :
#     print("You can't drive ")
    
    

# a=7
# b=1
# c=10

# if b<a>c:
#     print("a is greater")
# elif a<b>c:
#     print(" b is greater ")
# else:
#     print("c is greater")
    
# # typecasting 

# f = "67"
# print(type(f))
# f = float(f)
# print(f)


# a = 56
# b = 8
# a = str(a)
# b = str(b)
# print(a+b)


# while loops

# a = 100 
# flag =True 
# while flag  :
#     print(a)
#     a = a -1
#     if a>0 :
#         flag = False 

#start to end -1


# for a in range(100 , 0 , -1) :
#     print(a)
    

# break , continue 

# flag = True 
# while flag :
#     userin =  input()
#     if userin == "exit":
#         print("game over")
#         break;
    
# continue :  it make the control go to next interation 
# break :  ends the loop  , control goes outside the loop
for i in range( 1  ,50):
    if i%7==0 :
        print(i , end=" ")
        continue
    
    print(i , "n" , end=" ")

# Q1) 1 to N  , N is user input  and if i,th number is divisble by 5 then print Fibb  , if by 7 print Buzz and if by both print FizzBuzz  and if nothing print the number 
# Q2) 

'''
N=5
*
**
***
****
*****
*****
****
***
**
*

'''

