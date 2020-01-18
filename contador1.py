# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:27:10 2020

@author: Aluno
"""
n = 1
soma = 0
while n <= 10:
    x = int(input("digite o %d numero: " %n))
    soma += x
    n = n + 1
print ("soma: %d" %soma)