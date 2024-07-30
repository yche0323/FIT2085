def read_integers():
    i = input("Enter some integers: ").split()
    print(i)


read_integers()


def sum_squared_integers(array):
    sq = []
    for i in array:
        sq.append(i**2)
    print(sum(sq))


sum_squared_integers([])


def read_from_file_sum_squares():
    filename = input("Enter the filename: ")
    input_file = open(filename, "r")
    list_lines = int(input_file.readlines())
    sq = []
    for i in list_lines:
        sq.append(i**2)
    print(sum(sq))
    input_file.closed()


def read_from_file_table():
    filename = input("Enter the filename: ")
    input_file = open(filename, "r")
    list_lines = int(input_file.readlines())
    non_neg = []
    for item in list_lines:
        if item >= 0:
            non_neg.append(item)
    print(non_neg)
    input_file.closed()
