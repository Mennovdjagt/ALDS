def getNumbers(s):
    """Function that will return a list of only the numbers in a string.

       Args:
          lst (string): The first parameter needs to be a string

       Returns:
          The return value is a list of all the numbers in the string
       """
    lst = []
    buffer = ''
    for character in s:
        if character.isdigit():
            buffer += character
        elif not character.isdigit() and buffer:           #when it is no digit and there is something in the buffer, add the buffer to the lst
            lst.append(buffer)
            buffer = ''
    if buffer:                                      #if there is still something in the buffer and the for loop is done, add the buffer to the lst
        lst.append(buffer)
    return lst


text = 'een123zin45 6met-632meerdere+7777getallen88'
print(getNumbers(text))
