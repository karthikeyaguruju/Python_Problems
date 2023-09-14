# using random Module in Chocie --> in bulit function
[Taking Inputs]
import random

names=['karthikeya','karthik','deepak','vijay']
b=random.choice(names)

print(f"{b} will pay the fill")
################################################
[Without Taking Inputs]

import random

names=input("Enter Everybody's name separated by comma :")

a=names.split(",")

selected=random.choice(a)

print(f"{selected} will pay the bill")
##########################################
# using random Module in randint --> in bulit function

import random

names=input("Enter everbody's name separated by comma:")

a=names.split(",")
n=len(a)
b=random.randint(0,n-1)

print(f"{a[b]} will pay the fill")
