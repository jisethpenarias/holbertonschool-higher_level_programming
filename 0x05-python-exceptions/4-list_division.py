#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for num in range(list_length):
        try:
            div = my_list_1[num] / my_list_2[num]
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            result.append(div)
    return result
