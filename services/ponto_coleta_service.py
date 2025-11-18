import sqlite3
from datetime import datetime
from database.database import get_connection
from database.models import PontoColeta

class PontoColetaService:
    
    def adicionar_ponto(self, ponto):
        conn = get_connection()
        cursor = conn.cursor()
        
        # Adicionar data atual automaticamente
        data_atual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
            INSERT INTO pontos_coleta 
            (nome, endereco, cidade, estado, telefone, horario_funcionamento, tipos_materiais, data_criacao)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (ponto.nome, ponto.endereco, ponto.cidade, ponto.estado, 
              ponto.telefone, ponto.horario_funcionamento, ponto.tipos_materiais, data_atual))
        
        conn.commit()
        ponto.id = cursor.lastrowid
        conn.close()
        return ponto
    
    # ... outros métodos permanecem iguais