# -*- coding: utf-8 -*-
""" ====================================

@name: matematica.py
@author: julio.nardelli
@data: 31-03-2020
@descricao: funções matemáticas
    
===================================== """

# =======================================
# Declaração de variáveis
# =======================================
PRECISAO = 1E-5

# =======================================
# Definição de procedimentos
# =======================================

""" ====================================

@name: xvpl (vpl expandido, fluxo de caixa não períodico)
@arg: 
        capital - investimento
        data_inicial - D "zero", data do investimento
        N - vencimentos
        i - taxa interna de retorno (TIR)
@result: ca
@info: calcula o valor presente líquido (VPL) em um fluxo de caixa não períodico
@fonte: https://www.ablebits.com/office-addins-blog/2019/07/24/excel-xirr-nonperiodic-cash-flows/

==================================== """
def xvpl(capital, data_inicial, N, i):
    result = -capital
    for n in N:
        delta = n.vencimento - data_inicial
        result += n.valor / ((1 + i) ** (delta.days / 365))
    return result

""" ====================================

@name: xtir (tir expandido)
@arg: 
        capital - investimento
        N - vencimentos
        imin - tir minimo da faixa de teste
        imax - tir maximo da faixa de teste
@result: ca
@info: calcula a taxa interna de retorno anual (a.a) de forma heurística em um fluxo de caixa não períodico
@fonte: https://www.ablebits.com/office-addins-blog/2019/07/24/excel-xirr-nonperiodic-cash-flows/

==================================== """
def xtir(capital, data_inicial, N, imin, imax):
    imedio = (imin + imax) / 2
    v = xvpl(capital, data_inicial, N, imedio)
    if (v >= -PRECISAO and v <= PRECISAO):
        return imedio
    elif (v > 0):
        return xtir(capital, data_inicial, N, imedio, imax)
    elif (v < 0):
        return xtir(capital, data_inicial, N, imin, imedio)