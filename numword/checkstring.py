import os
from django.shortcuts import render
mapping = {'10': 'Ten', '20': 'Twenty', '30':'Thirty', '40':'Fourty', '50':'Fifty', '60':'Sixty', '70':'Seventy', \
          '80':'Eighty', '90':'Ninety'}


def check10to90(number):
    actual_number = int(number)

    if actual_number == 0:
        numberw = 'and'
        return numberw
    if actual_number == 1:
        numberw = 'One'
        return numberw
    if actual_number == 2:
        numberw = 'Two'
        return numberw
    if actual_number == 3:
        numberw = 'Three'
        return numberw
    if actual_number == 4:
        numberw = 'Four'
        return numberw
    if actual_number == 5:
        numberw = 'Five'
        return numberw
    if actual_number == 6:
        numberw = 'Six'
        return numberw
    if actual_number == 7:
        numberw = 'Seven'
        return numberw
    if actual_number == 8:
        numberw = 'Eight'
        return numberw
    if actual_number == 9:
        numberw = 'Nine'
        return numberw
