#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random,readJSON

data = readJSON.readJsonFile("data.json")
famous = data["famous"] # a 代表前面垫话，b代表后面垫话
before = data["before"] # 在名人名言前面弄点废话
after = data['after']  # 在名人名言后面弄点废话
bosh = data['bosh'] # 代表文章主要废话来源

title = "学生会退会"

repeat = 2

def 洗牌遍历(myLst):
    global repeat
    pool = list(myLst) * repeat
    while True:
        random.shuffle(pool)
        for each in pool:
            yield each

nextBosh = 洗牌遍历(bosh)
nextFamous = 洗牌遍历(famous)

def 来点名人名言():
    global nextFamous
    xx = next(nextFamous)
    xx = xx.replace(  "a",random.choice(before) )
    xx = xx.replace(  "b",random.choice(after) )
    return xx

def 另起一段():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    xx = input("请输入文章主题:")
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            branch = random.randint(0,100)
            if branch < 5:
                tmp += 另起一段()
            elif branch < 20 :
                tmp += 来点名人名言()
            else:
                tmp += next(nextBosh)
        tmp = tmp.replace("x",xx)
        print(tmp)