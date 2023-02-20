# functions , void and return  , global and local variable 
# write a function to print triangular pattern , 2) pallindrome check  3) calculate factorial 
# 4) check is number is prime 5) sum of n natural numbers 6)swap two numbers 
# 7) find 2nd  largest number in a list 

#file handling(text file)
# 1) count the number of words in a text file 
# 2) implement search and replace feature in a text file 


# factorial 

# repeat your self 
# length 
# complex 
# error


# n! = 1*2*3*4....n

n=3




def fac(n):
    fac=1
    for i in range(1,n+1):
        fac = fac * i
    return fac
# calling 

# a=5
# b=7

a=7
b=5

a=b
a=5
b=a

def swap(a , b):
    temp = a
    a=b
    b=temp

a=5
b=7

a,b=b,a
swap(a,b)
print(a , b)

    

arr = [1,5,8,9,4,6,8]

# sort()
# arr[len(arr) -1]

# print(arr)



# for i in range(0, len(arr)-1):
#     if arr[i]<arr[i+1] :
#         pass
#     else:
#         arr[i] ,arr[i+1] = arr[i+1] , arr[i]

# print(arr)
# print(arr[len(arr) -1])



#max 
# global and local variables 

pi =3.14
# global variable 

def area(l,b):
    #local
    return l*b



# calling


print(area(2,5))
    
# defualt 

# for i in range(0,9 ,1 ):
#     print(i)
    
# variable arguments 
# list 

def add(*arg):
    sum =0 
    for i in arg :
        sum = sum + i
    return sum
    
print(add(1,2,3 , 888 , 5 , 7 ,8))
    
def greet(name , age):
    print("hello " + name + str(age))
    
 

# positional arguments
greet("Abhijeet" , 21)
# keyword arguments  
greet( age = 18  ,name = "Abhijeet" )
    
    
    
    
    
    
    
    
    
    


