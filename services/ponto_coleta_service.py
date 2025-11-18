import sqlite3
from database.database import get_connection
from database.models import PontoColeta

class PontoColetaService:
    
    @staticmethod
    def criar_ponto_coleta(ponto_coleta):
        """Cria um novo ponto de coleta"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO pontos_coleta 
            (nome, endereco, cidade, estado, telefone, horario_funcionamento, tipos_materiais)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ponto_coleta.nome, ponto_coleta.endereco, ponto_coleta.cidade,
              ponto_coleta.estado, ponto_coleta.telefone, 
              ponto_coleta.horario_funcionamento, ponto_coleta.tipos_materiais))
        
        conn.commit()
        ponto_id = cursor.lastrowid
        conn.close()
        
        return ponto_id
    
    @staticmethod
    def listar_pontos_coleta():
        """Lista todos os pontos de coleta"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, nome, endereco, cidade, estado, telefone, 
                   horario_funcionamento, tipos_materiais, data_criacao, data_atualizacao
            FROM pontos_coleta 
            ORDER BY data_criacao DESC
        ''')
        
        pontos = []
        for row in cursor.fetchall():
            ponto = PontoColeta(
                id=row[0], nome=row[1], endereco=row[2], cidade=row[3],
                estado=row[4], telefone=row[5], horario_funcionamento=row[6],
                tipos_materiais=row[7]
            )
            pontos.append(ponto)
        
        conn.close()
        return pontos
    
    @staticmethod
    def buscar_ponto_por_id(ponto_id):
        """Busca um ponto de coleta pelo ID"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, nome, endereco, cidade, estado, telefone, 
                   horario_funcionamento, tipos_materiais
            FROM pontos_coleta WHERE id = ?
        ''', (ponto_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return PontoColeta(
                id=row[0], nome=row[1], endereco=row[2], cidade=row[3],
                estado=row[4], telefone=row[5], horario_funcionamento=row[6],
                tipos_materiais=row[7]
            )
        return None
    
    @staticmethod
    def atualizar_ponto_coleta(ponto_coleta):
        """Atualiza um ponto de coleta existente"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            UPDATE pontos_coleta 
            SET nome = ?, endereco = ?, cidade = ?, estado = ?, telefone = ?,
                horario_funcionamento = ?, tipos_materiais = ?, data_atualizacao = CURRENT_TIMESTAMP
            WHERE id = ?
        ''', (ponto_coleta.nome, ponto_coleta.endereco, ponto_coleta.cidade,
              ponto_coleta.estado, ponto_coleta.telefone, 
              ponto_coleta.horario_funcionamento, ponto_coleta.tipos_materiais,
              ponto_coleta.id))
        
        conn.commit()
        conn.close()
        
        return True
    
    @staticmethod
    def excluir_ponto_coleta(ponto_id):
        """Exclui um ponto de coleta"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM pontos_coleta WHERE id = ?', (ponto_id,))
        
        conn.commit()
        conn.close()
        
        return True