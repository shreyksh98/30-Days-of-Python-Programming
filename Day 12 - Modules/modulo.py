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

def gen_hex():
    len = 6
    a = 'abcdef'
    hex = str(''.join(random.choices(string.digits+a, k = len)))
    hex = '#'+hex
    return hex

def list_of_rgb_colors(args):
    lst = []
    for i in range(0,args):
        r = randint(0,255)
        g = randint(0,255)
        b = randint(0,255)
        rgb = r,g,b
        rgb = 'rgb'+str(rgb)
        lst.append(rgb)
    return lst

def generate_colors(col, len):
    if col == 'hexa':
        hx_lst = []
        for i in range(0,len):
            len = 6
            alph = 'abcdef'
            hexa = "".join(random.choices(string.digits+alph, k=len))
            hexa = '#'+str(hexa)
            hx_lst.append(hexa)
        return hx_lst
    
    elif col == 'rgb':
        rgb_lst = []
        for i in range(0,len):
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            rgb = r,g,b
            rgb = 'rgb'+str(rgb)
            rgb_lst.append(rgb)
        return rgb_lst
    
    else:
        return("Wrong Input")
            
def shuffle_list(args):
    random.shuffle(args)
    return args

def rand_int():
    num = 0,1,2,3,4,5,6,7,8,9
    ran_lst = list(random.sample(num,k=7))
    return ran_lst
        


    

