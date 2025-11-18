import sqlite3
import streamlit as st
from datetime import datetime

def criar_tabela():
    """Cria a tabela de pontos de coleta se não existir"""
    conn = sqlite3.connect('pontos_coleta.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pontos_coleta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            telefone TEXT,
            horario_funcionamento TEXT,
            tipos_materiais TEXT,
            data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            data_atualizacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def get_connection():
    """Retorna uma conexão com o banco de dados"""
    return sqlite3.connect('pontos_coleta.db')