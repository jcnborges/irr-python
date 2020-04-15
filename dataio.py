# -*- coding: utf-8 -*-
import csv
import sqlite3
import pandas
import requests
import json
from datetime import datetime

""" ====================================

@name: dataio.py
@author: julio.nardelli
@data: 31-03-2020
@descricao: entrada/saída de dados
    
===================================== """

# =======================================
# Declaração de variáveis
# =======================================
NOME_MESES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

CREATE_TABLE_ATIVOS = """
    CREATE TABLE ativos(
        nome TEXT NOT NULL,
        valor FLOAT NOT NULL,
        vencimento DATE NOT NULL
    );
"""

CREATE_TABLE_RESULTADOS = """
    CREATE TABLE resultados(
        data_base DATE NOT NULL,
        irr FLOAT NOT NULL,
        selic FLOAT NOT NULL
    );
"""

INSERT_ATIVO = """
    INSERT INTO ativos VALUES("{0}", {1}, "{2}");
"""

INSERT_RESULTADO = """
    INSERT INTO resultados VALUES("{0}", {1}, {2});
"""

SELECT_ATIVOS = """
    SELECT *
    FROM ativos
    ORDER BY vencimento
"""

SELECT_RESULTADOS = """
    SELECT *
    FROM resultados
    ORDER BY data_base
"""

# FONTE: https://dadosabertos.bcb.gov.br/dataset/11-taxa-de-juros---selic/resource/3d751a0d-afb2-452b-83f2-310a201f8a82
SELIC_API = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados/ultimos/1?formato=json"

# =======================================
# Declaração de inner class
# =======================================
class Ativo : 
    def __init__(self, nome, valor, vencimento):
        self.nome = nome
        self.valor = valor
        self.vencimento = vencimento
        
    def __str__(self):
        return "nome = {0}; valor = {1}; vencimento = {2}".format(self.nome, self.valor, self.vencimento)
    
class Selic:
    def __init__(self, data, valor):
        self.data = data
        self.valor = valor

    def __str__(self):
        return "data = {0}; valor = {1}".format(self.data, self.valor)

class Resultado:
    def __init__(self, data_base, irr, selic):
        self.data_base = data_base
        self.irr = irr
        self.selic = selic

# =======================================
# Definição de procedimentos
# =======================================
def lerCSV(caminho):
    result = []
    with open(caminho) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            result.append(row)
        del result[0]
    return result

def csvToListAtivos(rows):
    result = []
    for row in rows:
        a = Ativo(
                row[0]
                ,float(row[1].replace("R$", "").replace(".", "").replace(",", ".").strip())
                ,datetime.strptime(row[2], "%d/%m/%Y").date()
            )
        result.append(a)
    return result
        
def criarDB():
    conn = sqlite3.connect(":memory:")
    executeSQL(CREATE_TABLE_ATIVOS, conn)
    executeSQL(CREATE_TABLE_RESULTADOS, conn)
    return conn

def executeSQL(sql, conn):
    cursor = conn.cursor()
    cursor.execute(sql)    

def insertAtivo(ativo, conn):
    sql = INSERT_ATIVO.format(ativo.nome, ativo.valor, ativo.vencimento)
    executeSQL(sql, conn)

def insertResultado(resultado, conn):
    sql = INSERT_RESULTADO.format(resultado.data_base, resultado.irr, resultado.selic)
    executeSQL(sql, conn)
    
def selectSQL(sql, conn):
    return pandas.read_sql_query(sql, conn)

def getSelic():
    result = []
    s = requests.Session()
    r = s.get(SELIC_API)
    listJsonSelic = json.loads(r.text)
    for jsonSelic in listJsonSelic:
        result.append(Selic(datetime.strptime(jsonSelic["data"], "%d/%m/%Y").date(), float(jsonSelic["valor"])))
    s.close()
    return result

def dataFrameToListAtivos(df):
    result = []
    for index, row in df.iterrows():
        a = Ativo(
                row["nome"]
                ,float(row["valor"])
                ,datetime.strptime(row["vencimento"], "%Y-%m-%d").date()
            )
        result.append(a)
    return result
    
