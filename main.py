# Các kiểu dữ liệu trong Python: String int float bool
""" = 3
b = 3.4
c = "Hello"
d = True

print(a)
print(b)
print(c)
print(d)
"""
# Comment:
# Input trong python: input() -> string , int: int(input()), double: double(input())
#   -> e = input()

# Nhap vao 2 so -> tinh tong 2 so day -> in ra man hinh
#print(e)
# e = int(input()) # "1"
# a = int(input()) # "2"
# print (   e + a ) # "12"
# Cho chieu dai, chieu dong dc input tu ban phim -> tinh dien tich hinh chu nhat
#d = int(input())
#r = int(input())
#print ( d * r)

"""Operator: + - * / // %
a = 11
b = 4

print(a / b) # 2.75
print(a // b) # int
print(a % b) # chia lấy dư

# **: số mũ trong python
print(a**b) ## 11 mũ 4
# a += 1 :toán tử 1 ngôi  (không có a++)

BT: Nhap 1 so, va check so do > 0 hay ko -> > 0 positive 
< 0 negative
a = int(input())
if  a > 0:
    print ( 'positive number' )
elif a == 0:
    print("Equals 0")
else:
    print ( 'negative number')
    
Problem: Grade classification: Input an integer score (ranging from 0 to 100) and classify the grade:
-> "Weak" if score <= 50.
-> "Average" if 50 < score <= 60.
-> "Good" if 60 < score <= 75.
-> "Very Good" if 75 < score <= 90.
-> "Excellent" if the score is > 90.
a = int (input())
if a <= 50 : print ('weak')
elif a <= 60 : print ('Average')
elif a <= 75 : print (' Good')
elif a <= 90 : print (' very good')
else : print (' excellent')

|| && -> and or

Problem 4: Check if a year is a leap year: Input an integer year from the keyboard and determine if it's a leap year.
Print: "Year <year> is a leap year!" if it is.
Print: "Year <year> is not a leap year!" if it isn’t. 
-> Rules:
A year is a leap year if it is divisible by 4 but not divisible by 100, or it is divisible by 400.
a = int ( input ())
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
    print( f'year {a} is a leap year')
else : print( f'year {a} is not a leap year')

# if a "%" 2 == 0

Problem 7: Swap values of two integers: Input two integers a and b. Swap their values so that:
a becomes the value of b.
b becomes the value of a.
Print the result after the swap.
a = 3
b = 4

a , b = b , a # swap gia tri
print(a)
print(b)

Problem 5: Print the name of the day of the week: Input an integer from 0 to 6 and print the corresponding day name:
0: "Sunday".
1: "Monday".
2: "Tuesday".
3: "Wednesday".
4: "Thursday".
5: "Friday".
6: "Saturday". 
-> Requirements: 
Use if / elif / else
a = int ( input ())
if a == 0 : print ( ' Sunday')
elif a == 1 : print ( ' Monday')
elif a == 2 : print ( ' Tuesday')
elif a == 3 : print ( ' Wednesday')
elif a == 4 : print ( ' Thursday')
elif a == 5 : print ( ' Friday')
elif a == 6 : print ( ' Saturday')

In ra các số từ 0 -> 5:
for int i = 0 ; i <= 5 ; i ++
         start   end      step
         
In ra cac so tu -5 -> 10         
"""
#for i in range(0,  5 + 1 ,1): start end (+1) step
#    print(i, end=" ")
# for i in range( -5, 10 + 1, 1 ) :
#     if i % 2 != 0:
#         print( i, end=' ')
"""
Exercise 1: Display Even Numbers and Calculate Their Sum
Task:
Write a program that takes an integer n as input, displays all even numbers from n up to 100,
and calculates the sum of these even numbers.
Input:
An integer n (e.g., 90).
Output:
All even numbers from n to 100 (e.g., 90 92 94 96 98 100).
The sum of these even numbers (e.g., Sum = 570).
n = int ( input())
sum = 0
for i in range( n, 100 + 1, 1):
    if  i % 2 == 0:
        print(i, end= " ")
        sum += i

print ( sum ) # 1950

Exercise 2: Numbers Divisible by 3 and 5
Task: Write a program that takes two integers a and b and displays all numbers between them divisible by both 3 and 5.
Steps:
Input two integers a and b.
Loop through numbers from a to b. 
Check if each number is divisible by both 3 and 5.
Print the valid numbers.
Input:
Two integers a and b (e.g., 1 and 50).
Output:
All numbers = divisible by both 3 and 5 (e.g., 15 30 45).
a = int (input())
b = int (input())
for i in range( a, b + 1, 1):
    if i % 3 == 0 and i % 5 == 0:
        print( i, end=' ')
        
Exercise 6: Count Divisors
Task: Write a program that inputs an integer n and displays the number of its divisors.
Steps:
Input an integer n.
Loop through numbers from 1 to n.
Check if each number divides n evenly.
Count and print the divisors.
Input:
An integer n (e.g., 12).
Output:
Number of divisors (e.g., 6 for 12). Nhập 2 số a,b (a <b) .
n = int ( input()) # 20
count = 0

for i in range( 1, n + 1, 1):
    if n % i == 0:
        count+= 1
        print( i, end=" ")
print (count)

** BT:  In ra 3 số đầu tiên trong khoảng a,b chia hết cho 3 hoặc 7
VD: a = 1 - b = 50 -> output: 3 6 7 (hint: break)

a = int (input ())
b = int (input())
count = 0
for i in range( a, b + 1, 1):
    if i % 3 == 0 or i % 7 == 0 :
        count += 1
        print( i , end= " ")
    if count == 3:
        break

Exercise 10: Shape Calculator
Task: Develop a program to calculate the perimeter and area of shapes based on a menu of options.
Menu:
1. Calculate the perimeter and area of a rectangle.
2. Calculate the perimeter and area of a triangle.
3. Calculate the perimeter and area of a circle.
4. Exit.
while True:
    print("Menu:")
    print("1. Calculate the perimeter and area of a rectangle:")
    print("2. Exit.")
    choice = int(input())
    if choice == 1:
        print("Area")
    elif choice == 2:
        exit()
        
while True:
    choice -> input
    if- elif - else:
    exit(): hàm để thoát chương trình
while True:
print('Menu: ')
print('1. Coke')
print('2, Pepsi')
print('3, Water')
print('4, Coffe')
print('5, Exit Menu')
print('Enter your choice: ')
choice = int(input())
if choice == 1:  print('$1.25')
elif choice == 2: print ( '$1.00')
elif choice == 3: print ( ' $2.00')
elif choice == 4: print ( '$1.50 ')
elif choice == 5:  break()
Exercise 13: Validate User Input
while True:
    age = int(input())
    if age > 120 or age < 0: print("Err")
    else:
        print(age)
        break()
"""
a = 50
count = 0
while True:
    choice = int( input ())
    if choice < a :
        count +=1
        print ('too low')
    elif choice > a :
        count += 1
        print ('too high')
    elif choice == a:
        count += 1
        print ( 'exactly')
        break # break

print(count)








