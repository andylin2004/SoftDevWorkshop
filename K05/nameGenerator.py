# Andy Lin
# SoftDev
# K05 - combining code between trios to make a better student RNG selector
# 2021-09-27

import random

crews = {
    'pd1': ['Owen Yaggy', 'Haotain Gan', 'Ishraq Mahid', 'Julia Nelson', 'Ivan Lam',
       'Michelle Lo', 'Christopher Liu', 'Michael Borzuk', 'Ivan Mijacika',
       'Lucas Lee', 'Rayat Roy', 'Emma Buller', 'Andrew Juang',
       'Renggeng Zheng', 'Angela Zhang', 'Alejandro Alonso', 'Deven Mahehwari',
       'Hebe Huang', 'Aryaman Goenka', 'Oscar Wang', 'Tami Takada', 'Yusuf Elsharawy',
       'Ella Krechmer', 'Tomas Acuna', 'Tina Nguyen', 'Sadid Ethun', 'Shyne Choi',
       'Shriya Anand', 'Lucas Tom-Wong', 'Theo Fahey', 'Sean Ging', 'Gavin'],
    'pd2': ['Patrick Ging', 'Raymond Yeung', 'Josephine Lee', 'Alif Abdullah',
       'William Chen', 'Justin Zou', 'Andy Lin', 'Rachel Xiao', 'Yuqing Wu',
       'Shadman Rakib', 'Liesel Wong', 'Daniel Sooknanan', 'Cameron Nelson',
       'Austin Ngan', 'Thomas Yu', 'Yaying Liang Li', 'Jesse Xie', 'Eric Guo',
       'Jonathan Wu', 'Zhaoyu Lin', 'Joshua Kloepfer', 'Noakai Aronesty',
       'Yoonah Chang', 'David Chong', 'Wen Hao Dong', 'Mark Zhu', 'Qina Liu',
       'Kevin Cao', 'Sophie Liu', 'Annabel Zhang', 'Roshani Shrestha', 'Han Zhang']
}


input = input("Input period number (1 or 2)")
if input.isnumeric() and input != "0":
    if input == "1":
        print(random.choice(crews.pd1))
    elif input == "2":
        print(random.choice(crews.pd2))
    else:
        print("invalid period--please try again")