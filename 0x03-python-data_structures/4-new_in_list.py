#!/usr/bin/python3
# 4-new_in_list.py
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    list_copy = [x for x in my_list]
    list_copy[idx] = element
    return (list_copy)
