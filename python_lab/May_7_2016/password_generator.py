#!/usr/bin/env python
# Password generator
#
#
#

import random
import string

print("Hello, world!")


def password_generator(length, has_num=True, has_punct=True, has_cap=True):

    # track how many letters we have already used
    used = 0

    #   lowers = 'abcdefghijklmnopqrstuvwxyz'
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    nums = string.digits
    puncts = string.punctuation

    if (length < has_num + has_punct + has_cap):
        raise Exception("Password length must be at least greater than " +
                        str(has_num + has_punct + has_num) + " in order " +
                        "to meet the constraints of the password.\n The " +
                        "length of your password is " + str(length) + ".")

    password = ''
    if (has_cap):
        password += random.choice(uppers)
        used = used + 1

    if (has_num):
        password += random.choice(nums)
        used = used + 1

    if (has_punct):
        password += random.choice(puncts)
        used = used + 1

    # password += ''.join([random.choice(lowers + uppers + nums + puncts)
    #                     for cnt in range(0, length - used)])
    password += ''.join([random.choice(lowers)
                         for cnt in range(0, length - used)])

    return "".join(random.sample(password, len(password)))

try:
    raw_password_length = input("How long should it be? ")
    password_length = int(raw_password_length)
    print(password_generator(password_length))

except ValueError:
    print("Please type a number for the length of the password!")
