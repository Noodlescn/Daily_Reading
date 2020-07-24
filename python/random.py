#!D:\Python3.8.5\Python38\python

import random
import string

a=string.ascii_letters + string.digits

key = []


def getKey():
    '生成32位随机数'
    key = random.sample(a, 32)
    keys = "".join(key)
    return keys