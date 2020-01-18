# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 17:27:10 2020

@author: Aluno
"""
soma = 0
n = 0
while True:
    x = int(input("Digite o número(0 sai):"))
    if x == 0:
        break
    else:
        n = n + 1
    soma = soma + x
print ("Média: %5.2f" %(soma/n))