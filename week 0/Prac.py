# function
def funny(x, y, z):
    while x >= y:
        x = x - z
        print(x)


funny(20, 4, 7)

my_list = [1, 2, 3.5, 'ho']

# the first element starts at 0
first_element = my_list[0]
print(first_element)

# length of the array
length = len(my_list)
print(length)

# slicing does not include the higher index: array[lower_index: higher_index]
slicing_1 = my_list[1:3]
slicing_2 =my_list[:3]
print(slicing_1)
print(slicing_2)


# for loop
def print_all(the_list):
    for item in the_list:
        print(item)


print_all(my_list)


# Loop a fixed number of iterations; n times
def repeat(n):
    for i in range(n):
        print(i)


repeat(3)


def also_funny(x, a_list):
    for item in a_list:
        if item > 0:
            result = x + item
            print(result)


also_funny(10, [-5, 2, 0])
