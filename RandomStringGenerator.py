# Konstantinos Malamas 2748
# Random String Generator to test the algorithms. It generates two strings with n length, and d different digits

import random
from random import randrange


def generate_random_strings(n, d):  # n is for

    a_string = []
    d_array = [True for y in range(n)]  # the positions of the seats that we'll change
    new_d = []

    for i in range(d):
        while True:
            possition = randrange(n)
            if d_array[possition]:
                d_array[possition] = False
                new_d.append(possition)
                break
    print(new_d)

    zero_sum = 0
    one_sum = 0
    for i in range(n):
        random_number = random.random()  # gives random number between 0 and 1
        if random_number < 0.5:
            a_string.append("0")
        else:
            a_string.append("1")

    b_string = list(a_string)

    for j in new_d:
        if b_string[j] == "0":
            b_string[j] = "1"
        else:
            b_string[j] = "0"

    #print("a_string: ", a_string)
    #print("b_string:", b_string)
    return a_string, b_string

