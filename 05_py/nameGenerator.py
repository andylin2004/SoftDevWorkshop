# Andy Lin
# SoftDev
# K05 - combining code between trios to make a better student RNG selector
# 2021-09-27

# Summary of trio discussion
# We discussed about how to combine code together and learning how each other's code worked and learned what was the good parts of each code (my input selector, file structure of Jonathan's, and Wenhao's random choice thing)

# Discoveries
# We found out that we could probably just use random.choice when we are selecting a random item from a dictionary, as well as building the database within the file instead of accessing an outside file.

# Questions
# No questions at all.

# Comments
# We should've used GitHub to get all the students names instead of using placeholder names

# get random library
import random

# class list for both periods
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

# get input of what period the user wants to get random person
input = input("Input period number (1 or 2)")
# see if period 1 or 2, or invalid input
if input == "1":
    # get random person from period 1
    print(random.choice(crews['pd1']))
elif input == "2":
    # get random person from period 2
    print(random.choice(crews['pd2']))
else:
    # tell user they put invalid option
    print("invalid period--please try again")