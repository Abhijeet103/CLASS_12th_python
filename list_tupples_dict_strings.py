# #Data Structure basic , Sequential and non sequntial , physical and logical ds
# #List (append , pop , insert , sort , search , len , slicing )
# #tupples 
# #strings 
# #Dictanories 
# #functions

# marks = [10,12,34,5,6,8,9,0,6,7,9,1,3,5,7 ,"abhijeet" , True]

# #index 
# print(marks[-5])
# print(marks[5])
# #slicing(start to end-1)
# print(marks[2:7])
# print(marks[2:7:3])
# print(marks[7:2:-1])
# #reverse 
# size = len(marks)
# l= size-1

# print(marks[16::-1])
# print(marks[:7])
# print(marks[3:])

# #list modification 
# print(marks)
# #last index
# marks.append(89)
# #pos , element 
# marks.insert(2,70)
# print(marks)
# #pop last element is deleted 
# marks.pop()
# print(marks)
# # pop(i)  will delted the ith element
# marks.pop(-2)
# print(marks)
# marks.clear()
# print(marks)


# #  user input and return index of that element 


# #linear search 
# arr=[2,4,5,6,7,2,5,6,7,7,7]
# key = 7

# for i in range(0 , len(arr)):
#     if key == arr[i]:
#         print(i)
#         break;
# count = 0
# #  frequency of the key
# for i in range(0 , len(arr)):
#     if key==arr[i]:
#       count = count +1


# print(count)

# #sum , count , max, min 

# sum =0 
# for i in range(0, len(arr)):
#     sum =sum +arr[i]
    
    
# print(sum)
 
# # implement  max min for a list     

# print(arr)
# arr.sort()
# print(arr)
# arr.sort(reverse=True)
# print(arr)



# # tupple 

# arr = [2,6,8,5,3]
# a2 = (2,6,8,5,3)

# #tupple --> list 

# a2 = list(a2)

# print(type(a2))
# print(type(arr))



# #  Dictanories

# menu  = { "pizza" : 40 , "soda":10 , "burger" : 20}

# print(menu["pizza"])
# # insertion 
# print(menu)
# menu.update({"samosa" : 5})
# print(menu)

# menu.pop("soda")



# print(menu)



# # for each loop 

# for i in menu :
#     print(i , menu[i])


# arr=[3,4,5,6,7,7]
# #  for each loop
# for i in arr :
#     print(i)
  

# for i in range(0 , len(arr)):
#     print(arr[i])





# menu , user will give input order and you hvae to calculate total bill 

# give your order and type exit to quit 

# menu = {"pizza" : 40 , "soda":10 , "burger" : 20}

# flag = True 

# sum =0 
# while flag :
#     userin = input()
#     if userin == 'exit':
#         break
#     price =  menu[userin]
#     sum = sum + price 

# print(sum)


# strings
a = "welcome to  our hotel " 

size = len(a)
print(size)
print(a[size-1])

print(a[size -1::-1])


for i in range(0 , size):
    print(a[i])
    
    
print(a)    
a =a.strip()
print(a)
# a.lower()
# a.strip() : removes unnessary space 


# important split function splits your string on the basis of a given chracter and converts it into a list
print(a.split(","))
print(a.replace("h" , 'm'))


first = "Abhijeet"
last = "jha"


name  = first +" "+ last 

print(name)


# previous year question 
# 2 Question   , min max of list implement 




