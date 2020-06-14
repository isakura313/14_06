# -*- coding: utf-8 -*-

import json
filename = 'data.json'
def greet(name):
    name = name.strip()
    with open(filename, "r") as f:
        username = json.load(f)
        if username['name'] == name:
            print(f" Welcome back  {username['name']}  {username['surname']}")
        else:
            print("Похоже вас нет в этой системе")


reg = input("Вы уже есть в системе? Если да, нажмите 1, 0 если нет")
if reg == "1":
    name = input("Введите ваше имя \n")
    greet(name)
elif reg == "0":
    name = input("Введите ваше имя \n")
    surname = input("Введите вашу фамилию")
    with open(filename, "a",  encoding = "utf-8") as f:
        data = {"name": name, "surname": surname}
        json.dump(data,f)
        print("Вы были зарегестрированы")
