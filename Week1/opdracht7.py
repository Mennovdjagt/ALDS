def find(lst, x):
    """Function that will search for x in the list lst and returns the index of x in lst.

       Args:
          param1 (list): The first parameter needs to be a list.
          param2: the second parameter is the value we want to find in the list

       Returns:
          The return value is the location of the value we want to find.
    """
    if len(lst) == 0:
        return -1
    if lst[-1] == x:
        return len(lst)
    return find(lst[0:-1], x)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(find(lst, 8))