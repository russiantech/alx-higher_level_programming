#!/usr/bin/python3
# replace without modifying the list index

def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    copy = [i for i in my_list]
    copy[idx] = element
    return (copy)