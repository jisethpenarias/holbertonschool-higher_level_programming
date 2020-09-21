#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    for element in my_list[0:x]:
        try: 
            print("{}".format(my_list[element]), end="")
            num += 1
        except:
            break
    print("")
    return num
