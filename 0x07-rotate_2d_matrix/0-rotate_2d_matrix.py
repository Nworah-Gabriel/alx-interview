#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """A function for rotating 2D matrix"""
    holder = []
    newlist = []

    matrix.reverse()
    if matrix is None:
        return
    for lists in matrix:
        count = 0
        for liss in lists:
            if type(liss) == list:
                return
        if len(holder) == 0:
            for liss in lists:
                newlist = []
                newlist.append(liss)
                holder.append(newlist)
        elif len(holder) != 0:
            number = len(holder)
            if count <= number:
                for liss in lists:
                    holder[count].append(liss)
                    count += 1

    matrix.clear()
    for lists in holder:
        matrix.append(lists)
