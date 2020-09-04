#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for name in dir(hidden_4):
        # if name[0:2] != "__":
        # if "__" not in name:
        # every comented if can be the solution
        if name.find("__") == -1:
            print(name)
