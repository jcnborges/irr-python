# -*- coding: utf-8 -*-
from matematica import *
from dataio import *
from datetime import date

""" ====================================

@name: main.py
@author: julio.nardelli
@data: 31-03-2020
@descricao: código principal
@requisitos:

- Read an CSV file with the assets - OK
- Calculate the IRR(You must create your own algorithm (don't use any python mathematical function for that) we want to test your logical thinking here - OK
- Consume a public web service that return the Selic rate of the day - OK
- Show the IRR calculated and the Selic rate in console - OK
- Store the information of the CSV file, the calculated IRR and Selic rate in a in memory database - Feel free to use structure or framework you like - OK
- Create a Docker image with the application ready to use;    

===================================== """

# =======================================
# Declaração de variáveis
# =======================================
CSV_FILE = "./Ativos.csv"
INVESTIMENTO = 300000

# =======================================
# Código principal
# =======================================
print("\nCarregando banco em memória...")
conn = criarDB()

print("\nCarregando CSV de ativos...")
rows = lerCSV(CSV_FILE)
ativos = csvToListAtivos(rows)

print("\nGravando ativos no banco...")
for ativo in ativos:
    insertAtivo(ativo, conn)

print("\nConsultando SELIC...")
selic = getSelic()[0]

print("\nRealizando cálculos...\n")    
dfativos = selectSQL(SELECT_ATIVOS, conn)
hoje = date.today()
print(dfativos)
xirr = 100 * xtir(INVESTIMENTO, hoje, dataFrameToListAtivos(dfativos), 0, 1)
xirr_dia = (1 + xirr) ** (1 / 365) - 1 # converte uma taxa anual para diária (FONTE: https://superuser.com/questions/352981/excel-formula-to-convert-per-annum-interest-rate-to-compounding-daily-and-weekly)
print("\nInvestimento = R$ {0:,.2f} \nIIR (a.a) = {1:.5f}% \nIIR (a.d) = {2:.5f}% \nSELIC (a.d) ({3:%d/%m/%Y}) = {4:.5f}%".format(INVESTIMENTO, xirr, xirr_dia, selic.data, selic.valor))    

print("\nConclusão... \nNa hipótese de você querer comprar hoje os ativos ou investir esse dinheiro a taxa SELIC do dia {0:%d/%m/%Y}, é melhor {1}".format(selic.data, "comprar os ativos." if xirr_dia > selic.valor else "emprestar a taxa SELIC."))

print("\nGravando resultados...")
resultado = Resultado(hoje, xirr_dia, selic.valor)
insertResultado(resultado, conn)

print("\nMostrando resultados gravados...\n")
dfresultados = selectSQL(SELECT_RESULTADOS, conn)
print(dfresultados)

print("\nFechando conexão...")

conn.close()    
    

