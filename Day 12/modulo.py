import random
from random import randint
import string

def random_string(s=6):
    rs = ''.join(random.choices(string.ascii_lowercase + string.digits, k = s))
    return rs

def user_id_gen_by_user(loop, len):
    for i in range(loop+1):
        rs = ''.join(random.choices(string.ascii_lowercase+string.digits, k=len))
        print(rs)

def rgb_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return(r,g,b)

# def gen_hex():
