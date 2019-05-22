#NUSH HACK - 
s = """
from games import *
from munprog import actual_mun
from plotting import *
from utilities import *
from Docs import documentation
from CeusGuru import lesson as learn

from math import *
import matplotlib.pyplot as plt
from turtle import *
import random
from random import choice as c
from random import randint as rand
from random import shuffle as shf
from time import sleep as s
import datetime
from calendar import month
import os
import webbrowser as wb
from googlesearch import search
"""

f = """
def GSearch():
    print('Enter Question')
    query = input()
    for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
        wb.open_new("https://google.com/search?q=%s" % query)
"""
from pytools import pythonshellreact
pythonshellreact(libs=s, funcs=f)

