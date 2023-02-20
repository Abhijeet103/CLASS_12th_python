
# check if the number is  prime number or not 


# 27 

# 1 ,2,3,4,5,.....27 

# 1 , n 

# 27 = 3 
#n=int(input("Enter the Number:"))


# #2 to n-1
# count = 0
# for i in range(2, n):
#     count = count +1 
#     if n%i==0:
#         print("It is not a prime number")
#         break;

# if count == n-2 :
#     print("prime")
    
    
# def checkprime(n) :
#     count = 0
#     for i in range(2, n):
#         count = count +1 
#         if n%i==0:
#             return False
        
    
#     if count == n-2 :
#         return True


    
# print(checkprime(n))

# 9 
# 9/1  
# 9/2 

 
 # precedence
 
 
print(2**4/2)

# ()
# **
# * ,  / , // , %
# +, -  
# # comparison operator == , >= , <= , < >
# not 
# and 
# or 
# #assingment operators = , += ,*=  , /=


# count  = count  +1 

# count += 1

# count *= 2

# count  = count*2

# count /= 3

# count  = count /3



#print(3*7//8+3-7+(2-1))

# 3*7//8+3-7+1

# 21//8+3-7+1

# 2+3-7+1
# -1



#precedence is same then you follow associativity
# left to right

# right to left  :  ** , = ,+=


#16 

#print(2**3**2)




#64

# binary file handling 


#text  , binary , csv(import csv) 

import pickle

#{data}--->  byte stream  :  pickling

f = open("demofile.dat" ,'wb')
x = [5,8,9,0]
pickle.dump(x,f)
#dump :  writing


f =  open('demofile.dat' , 'rb')
data  = pickle.load(f)
print(data)

#load : reading

#file handling
------


# # # ram  temp

# # #  files 

# # # f = open("demofile.txt" , 'r')
# # # # read mode 
# # # # paramter  in read(x) x :  no of characters 
# # # # space is also a character 


# # # # write mode : all previous data will be deletd and new data will be written on 
# # # f = open("demofile.txt" , 'w')


# # # f.write("i am from jaipur")

# # # # append mode 

# # # f = open("demofile.txt" , 'a')


# # # f.write("i am from jaipur")


# # # read the file and return the number of words 
# # # strings
# # # 

# # f =  open("demofile.txt" , 'r') 

# # str = f.read()
# # #str.strip()
# # str = str.split(" ")
# # # print(str)
# # print(len(str))


# ##
# import csv 

# f = open("data.csv" ,'w')


# # rows = csv.DictReader(f)

# # for i in rows :
# #     print(i)


# wr =  csv.DictWriter(f)

# wr.writeheader({"name" ,"age"})



# # rows is in the form of 2d list [[],[]]
# # rows = csv.reader(f)

# # buyers avg age = total age / no of buyers 

# # sum =0 
# # len =0 
# # rows = list(rows)
# # rows.pop(0)



# # for i in rows:
# #     sum = sum  + int(i[0])
# #     len = len +1

# # avg = sum/len

# # print(avg)
# # # age 

# # arr1 = [[3,5,6],[4,7,8],[6,7,8], [6,7,8]]

# # arr =[1,52,35,4,55,6]

# # for i in range(0 , len(arr)):
# #     print(arr[i])

# # elementts of the list = i 
# # for i in arr:
# #     print(i)

# # for i in arr1:
# #     print(i)


# # for i in rows :
# #     print(i)



# # list format 

# # [[] ,[],[]]

# # wr.writerow(['23' ,'1' , '1'])

# # wr.writerows([[24,5,7],[32,4,8]])



# # reader
# # writer 

# #DictReader
# #DictWriter

# #tupple - >list 

import pickle

f = open("demofile.dat" ,'wb')
x = [5,8,9,0]
pickle.dump(x,f)
# dump :  writing


f =  open('demofile.dat' , 'rb')
data  = pickle.load(f)
print(data)

#load : reading














