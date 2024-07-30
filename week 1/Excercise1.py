def mystery(my_list):
    my_list = []
    count = 0
    add =0
    i = 0
    while i < my_list.length:
        print("Outside")
        count = count + 1
        add = add + my_list[i]
        j = 0
        while j < my_list.length:
            print("Inside")
            count = count + 1
            add = add + my_list[i]
            j = j + 1

        i = i + 1

    print("Addition: " + add)
    return count


mystery([1, 2, 3, 4, 5, 6, 7])
