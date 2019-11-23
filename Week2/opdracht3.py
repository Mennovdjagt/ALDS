from random import seed
from random import randint

def change_equal_numbers (x):
    """function that returns the changes of equal birthday's in 100 classes of 30 people

    Returns:
        float: the change of people having the same birthday

    Examples:
        >>> print(change_equal_numbers(5))
        1.31

    """

    seed(x)
    probability = 0  # saves every time a set is found in the birthday set

    for i in range(0, 100):
        birthday = set()  # saves all people in the class
        for j in range(0, 30):  # 30 people in a class
            value = randint(1, 356)  # random value between 1 and 356
            if value in birthday:  # checks if the value is equal to a element in the set
                probability += 1
            birthday.add(value)

    return probability / 100


print(change_equal_numbers(10))
