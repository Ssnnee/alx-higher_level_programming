#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """This function divides element by element 2 lists.

    Return:
        (list): A new list (length = list_length) with all divisions
    """

    new_list = [0] * list_length
    for i in range(list_length):
        try:
            if isinstance(my_list_1[i], (int, float)) and isinstance(
                my_list_2[i], (int, float)
            ):
                new_list[i] = my_list_1[i] / my_list_2[i]
            else:
                new_list[i] = 0
                print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return new_list
