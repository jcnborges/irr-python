# -*- coding: utf-8 -*-
from matematica import *
from dataio import *
from datetime import date

""" ====================================

@name: unit.py
@author: julio.nardelli
@data: 31-03-2020
@descricao: testes unitários
        
===================================== """

# =======================================
# Declaração de variáveis
# =======================================

CSV_FILE = "./ativo_teste.csv"

# =======================================
# Testes unitários
# =======================================

print("=======================================")
print("Leitura CSV")
print("=======================================")
rows = lerCSV(CSV_FILE)
for row in rows:
    print(row)
ativos = csvToListAtivos(rows)
for ativo in ativos:
    print(ativo)

print("=======================================")
print("Cálculo XVPL")
print("=======================================")
# Fonte: https://www.ablebits.com/office-addins-blog/2019/07/24/excel-xirr-nonperiodic-cash-flows/
hoje = datetime.strptime("01/01/2019", "%d/%m/%Y").date()
capital = 1000
i = 0.05
print("capital = {0} \ni = {1} \nXVPL = {2}".format(capital, i, xvpl(capital, hoje, ativos, i)))

print("=======================================")
print("Cálculo XTIR")
print("=======================================")
hoje = datetime.strptime("01/01/2019", "%d/%m/%Y").date()
capital = 1000
print("capital = {0} \nXTIR = {1}".format(capital, xtir(capital, hoje, ativos, 0, 1)))

print("=======================================")
print("SGBD in Memory")
print("=======================================")
conn = criarDB()
for ativo in ativos:
    insertAtivo(ativo, conn)
print(selectSQL(SELECT_ATIVOS, conn))
conn.close()

print("=======================================")
print("SELIC API")
print("=======================================")
selic = getSelic()
print(selic[0])