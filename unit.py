# -*- coding: utf-8 -*-
from matematica import *
from dataio import *
from datetime import date
import unittest

""" ====================================

@name: unit.py
@author: julio.nardelli
@data: 15-04-2020
@descricao: testes unitários
        
===================================== """

# =======================================
# Declaração de variáveis
# =======================================

CSV_FILE = "./ativo_teste.csv"

# =======================================
# Testes unitários
# =======================================

class TestCaseGeral(unittest.TestCase):
    
    def test_leituraCSV(self):
        rows = lerCSV(CSV_FILE)
        self.assertEqual(len(rows), 3)
        
    def test_conversaoCSVToAtivos(self):
        rows = lerCSV(CSV_FILE)
        ativos = csvToListAtivos(rows)
        self.assertEqual(len(rows), len(ativos))
        
    def test_sgbd(self):
        rows = lerCSV(CSV_FILE)
        ativos = csvToListAtivos(rows)
        conn = criarDB()
        for ativo in ativos:
            insertAtivo(ativo, conn)
        sql_ativos = selectSQL(SELECT_ATIVOS, conn)
        self.assertEqual(len(ativos), len(sql_ativos))
        
    def test_xvpl(self):
        rows = lerCSV(CSV_FILE)
        ativos = csvToListAtivos(rows)
        capital = 1000
        i = 0.05
        hoje = datetime.strptime("01/01/2019", "%d/%m/%Y").date()
        self.assertEqual(xvpl(capital, hoje, ativos, i), 68.96021027991259)
        
    def test_xtir(self):
        rows = lerCSV(CSV_FILE)
        ativos = csvToListAtivos(rows)
        capital = 1000
        hoje = datetime.strptime("01/01/2019", "%d/%m/%Y").date()
        self.assertEqual(xtir(capital, hoje, ativos, 0, 1), 0.08036087453365326)
        
    def test_selic(self):
        selic = getSelic()
        self.assertTrue(len(selic) > 0)
        self.assertFalse(len(selic) < 0)
        
if __name__ == '__main__':
    unittest.main()
