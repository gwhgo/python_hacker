#!/bin/python3
# coding=utf-8

import crypt
import re
def testPass(cryptPass):
    salt = re.match('.*\$',cryptPass).group()
    dict = open('dic','r')
    for word in dict.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word,salt)
        if (cryptWord == cryptPass):
            print("[+] Found Password: " + word + "\n")
            return
    print("Found not Password")

if __name__ =='__main__':
    passFile = open('/etc/shadow')
    password = passFile.readline().strip('\n')
    testPass(password.split(':')[1])
