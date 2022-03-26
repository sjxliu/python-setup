def hello():
    print("Hello user")
hello()

def pack(arg1, arg2, arg3):
    print(arg1 + ', ' + arg2+ ', ' +arg3)
pack('toothbrush', 'soap', 'underwear')

def eat_lunch(food_list):
    if len(food_list) == 0:
        print("Oh no my lunch box is empty :(")
    else:
        for x in range(len(food_list)):
            if x == 0:
                print(f'First I will be eating {food_list[0]}')
            else: 
                print(f'Next I will eat {food_list[x]} ')

eat_lunch(["stevia", "blueberries", "salt"])


print("---Python Functions Features 2---")

def arb_args(*names):
   for name in names:
        print("Hello", name)
arb_args('jeff', 'jace', 'jomama')

def func(a, b):
    def inner_1():
        return a+b
    def inner_2():
        return a-b
    print(inner_1()+inner_2())
func(5,4)

def lunch_lady(name, food='mystery meat'):
    print(name, food)
lunch_lady("steven")

def sum_n_product(x,y):
   print (x+y, x*y)
sum_n_product(2,3)

# superman = clark_kent

def num_average(*nums):
    sum_of_nums = 0
    count =0
    for num in nums:
        sum_of_nums += num
        count += 1
        average = sum_of_nums/count
    print(average)
num_average(3,5,2,63,65,12,4,23)


list1 = []



print("---Python Functions Features Part 3---")



print("---Python Functions Features Part 4---")

# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a,b,c):
    return max([a,b,c])

print(max_num(2343,7645,34))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def multiply_list(num_list):
    result = 1
    for x in num_list:
        result = result * x
    return result
list = [1,2,4]
print(multiply_list(list))

#Write a Python function called rev_string() to reverse a string.
def rev_string(my_str):
    return my_str[::-1]

if __name__ == "__main__":
    print(rev_string("steven"))

#Write a Python function called fib() to calculate the nth Fibbonacci number (a non-negative integer).
def fib(n):
    if n < 0:
        print("Unable to compute")
    elif n ==0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(4))

#Write a Python function called num_within() to check whether a number falls in a given range.
def within(n):
    if n in range(1, 100):
        print("Number is in range")
    else:
        print("Number is not in range")
within(45)

# or

def num_within(n, a, b):
    return n in range(a,b+1)
print(num_within(5,2,67 ))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# I strongly dislike math
tri = [[1], [1,1]]
def pascal(n):
    if n < 1:
        print("Cannot compute")
    elif n == 1:
        print(tri[0])
    else:
        row_num = 2
        while len(tri)<n:
            row = []
            row_prev = tri[row_num -1]
            length = len(row_prev)+1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(tri[row_num-1][i-1]+tri[row_num-1][i])
                else:
                    row.append(1)
            tri.append(row)
            row_num += 1
        for row in tri:
            print(row)
pascal(6)