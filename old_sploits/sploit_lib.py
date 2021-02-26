#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os,re
os.environ['PWNLIB_NOTERM'] = 'True'
from pwn import *

import string
import random

# global const
ENERGY_TO_CHANGE_POWER_SCHEME = 85.0

alph = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789'

boss_msgs = {
    b"You will die here. The sands will bury you and your memory will run out. All you can do is die worthy. You cannot survive in the sand, they will swallow you. And when you die, no one will regret. Surrender before it's too late and accept your death with dignity. Don't be a coward!": 0,
    b"Nowhere to run!": 1,
    b"You know my doom!! I will crush you": 2,
    b"You will stay here forever": 3}


def idg(size=8, chars=alph):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_correct_random_name():
    return idg(1, string.ascii_uppercase) + idg()


def generate_correct_random_password():
    password = idg(1, string.ascii_uppercase)
    tmp = idg(4, string.ascii_uppercase) + idg(4, string.ascii_lowercase) + idg(4, string.digits)
    tmp = list(tmp)
    random.shuffle(tmp)
    password += ''.join(tmp)

    return password


def reg_user(p, username, password):
    p.recvuntil("> ")
    p.send("2\n")
    p.recvuntil(": ")  # Enter username:
    p.send(username + '\n')

    buf = p.recv()

    if "User already exist!".encode() in buf:
        print("User is already registered!")
        return False

    p.send(password + '\n')

    return True


def login(p, username, password):
    p.recvuntil("> ")
    p.send("1\n")
    p.recvuntil(": ")  # Enter username:
    p.send(username + '\n')

    buf = p.recv()

    if "No such user!".encode() in buf:
        print("{-} User not found!")
        return False

    p.send(password + '\n')
    buf = p.recvline()

    if "Incorrect password".encode() in buf:
        print("{-} Password is invalid!")
        return False

    return True


def get_user_stats(p):
    p.recvuntil("[>] ")
    p.send("1\n")

    buf = p.recvuntil("{?}")
    ans = buf.decode()
    tmp_buf = ans.split('\n')[1:-1]

    for i in range(4):
        p.recvuntil(": ")
        p.send("n\n")

    stats = {}

    stats['name'] = tmp_buf[0].split(": ")[1]
    stats['status'] = tmp_buf[1].split(": ")[1]
    stats['actions'] = int(tmp_buf[2].split(": ")[1], 10)
    stats['hp'] = float(tmp_buf[3].split(": ")[1])
    stats['hunger'] = float(tmp_buf[4].split(": ")[1])
    stats['thirst'] = float(tmp_buf[5].split(": ")[1])
    stats['stamina'] = float(tmp_buf[6].split(": ")[1])
    stats['intelligence'] = float(tmp_buf[7].split(": ")[1])
    stats['repair_skill'] = float(tmp_buf[8].split(": ")[1])

    return stats


def read_book(p, count):
    p.recvuntil("[>] ")
    p.send('6\n')  # read book cmd

    p.recvuntil(": ")  # enter count
    p.send(str(count) + '\n')

    buf = p.recvuntil("|--")

    if "{+} You read the book".encode() in buf:
        return True
    else:
        return False


def go_to_next_day(p):
    p.recvuntil("[>] ")
    p.send("9\n")  # go to next day

    buf = p.recvline()

    if "Nothing happened".encode() in buf:
        return True
    else:
        print("Nigth event {}".format(buf))
        print("{-} You died!")
        return False


def eat_potato(p):
    p.recvuntil("[>] ")
    p.send("3\n")

    buf = p.recvline()

    if "{-} You don't have".encode() in buf:
        print("{-} No potatoes!")
        return False
    else:
        pass

    return True


def easy_raid(p):
    p.recvuntil("[>] ")
    p.send("7\n")  # make raid
    p.recvuntil(": ")  # choose difficult
    p.send("1\n")  # easy

    buf = p.recvline()
    if "{-} You do not have".encode() in buf:
        print("{-} No actions!")
        return False

    buf = p.recvrepeat(timeout=0.5)
    ans = buf.decode()
    #print(ans)
    new_ans = ans.split('\n')
    expr = new_ans[:-1][-1].split(' ')[0]

    x1, y1 = expr.split('+')

    answer = int(x1) + int(y1)
    p.send(str(answer) + '\n')

    buf = p.recvline()

    if "{+} You managed to open the chest and there you found:".encode() not in buf:
        print("{-} Erorr in easy raid (Code is correct, but chest not opened!")
        return False
    else:
        return True


def medium_raid(p):
    # valid code
    monster_hp = 120
    monster_attack = 12
    monster_regen = 8

    valid_code = monster_hp + monster_attack + monster_regen
    valid_code += int(get_user_stats(p)['hp'])
    valid_code = valid_code << 2
    valid_code += int(get_user_stats(p)['intelligence'])

    # ui part
    p.recvuntil("[>] ")
    p.send("7\n")  # make raid
    p.recvuntil(": ")  # choose difficult
    p.send("2\n")  # medium

    buf = p.recvline()
    if "{-} You do not have".encode() in buf:
        print("{-} No actions!")
        return False

    p.recvuntil("> ")

    while True:
        p.send("2\n")

        p.recvline()
        p.recvline()

        buf = p.recvline()
        valid_code += 13

        if "{+++} You killed a monster!!!".encode() in buf:
            break
        else:
            p.recvuntil("> ")

    p.recvuntil(": ")
    p.send(str(valid_code) + '\n')

    buf = p.recvline()

    if "{+} You managed to open the chest and there you found:".encode() not in buf:
        print("{-} Erorr in medium raid (Code is correct, but chest not opened!")
        return False
    else:
        return True


def make_valid_hard_raid_code(value, name):
    res = ''

    # first part
    value &= 0xff
    crc = 0xffff

    data = value
    data ^= crc & 255
    data ^= (data << 4) & 0xff

    t = (((data << 8) & 0xffff) | ((crc >> 8) & 255))
    t ^= (data >> 4) & 0xffff
    t ^= ((data << 3) & 0xffff)

    buf = str(t)

    if len(buf) != 5:
        buf = '0' * (5 - len(buf)) + buf

    res += str(t) + '-'

    # second part
    sym = (value ^ 65) & 0x7f
    buf = 'aaaa' + chr(sym)

    res += str(buf) + '-'

    # third part
    name_hash = hashlib.sha256(name.encode()).hexdigest()

    buf = name_hash[8]
    buf += name_hash[10]
    buf += name_hash[0]
    buf += name_hash[7]
    buf += name_hash[12]

    res += buf

    return res


def hard_raid(p, name):
    p.recvuntil("[>] ")
    p.send("7\n")  # make raid
    p.recvuntil(": ")  # choose difficult
    p.send("3\n")  # medium

    buf = p.recvline()
    if "{-} You do not have".encode() in buf:
        print("{-} No actions!")
        return False

    p.recvuntil("Boss says: ")
    message = p.recvuntil("\n").strip()
    p.recvuntil("> ")

    fight_sig = boss_msgs[message]

    while True:
        p.send("3\n")
        fight_sig += 3

        p.recvline()
        message = p.recvline().strip()

        if "{+} Wooo".encode() in message:
            break

        fight_sig += boss_msgs[message[len("Boss says: "):]]

        buf = p.recvuntil("> ")

    p.recvuntil(": ")  # code
    valid_code = make_valid_hard_raid_code(fight_sig, name)
    p.send(str(valid_code) + '\n')

    buf = p.recvline()

    if "{+} You managed to open the chest and there you found:".encode() not in buf:
        print ("{-} Erorr in hard raid (Code is correct, but chest not opened!")
        return False
    else:
        return True