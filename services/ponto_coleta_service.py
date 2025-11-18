import sqlite3
from datetime import datetime
from database.database import get_connection
from database.models import PontoColeta

class PontoColetaService:
    
    def adicionar_ponto(self, ponto):
        """Adiciona um novo ponto de coleta (alias para criar_ponto_coleta)"""
        conn = get_connection()
        cursor = conn.cursor()
        
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
    
    def criar_ponto_coleta(self, ponto):
        """Alias para adicionar_ponto - mantém compatibilidade"""
        return self.adicionar_ponto(ponto)
    
    def listar_pontos_coleta(self):
        """Lista todos os pontos de coleta"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, nome, endereco, cidade, estado, telefone, 
                   horario_funcionamento, tipos_materiais, data_criacao
            FROM pontos_coleta
            ORDER BY id DESC
        ''')
        
        resultados = cursor.fetchall()
        conn.close()
        
        pontos = []
        for resultado in resultados:
            ponto = PontoColeta(
                id=resultado[0],
                nome=resultado[1],
                endereco=resultado[2],
                cidade=resultado[3],
                estado=resultado[4],
                telefone=resultado[5],
                horario_funcionamento=resultado[6],
                tipos_materiais=resultado[7],
                data_criacao=resultado[8]
            )
            pontos.append(ponto)
        
        return pontos
    
    def buscar_por_id(self, id):
        """Busca um ponto de coleta pelo ID"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM pontos_coleta WHERE id = ?', (id,))
        resultado = cursor.fetchone()
        conn.close()
        
        if resultado:
            return PontoColeta(
                id=resultado[0],
                nome=resultado[1],
                endereco=resultado[2],
                cidade=resultado[3],
                estado=resultado[4],
                telefone=resultado[5],
                horario_funcionamento=resultado[6],
                tipos_materiais=resultado[7],
                data_criacao=resultado[8]
            )
        return None
    
    def excluir_ponto(self, id):
        """Exclui um ponto de coleta pelo ID"""
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute('DELETE FROM pontos_coleta WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return True
    
    def atualizar_ponto(self, ponto):
    """Atualiza um ponto de coleta existente"""
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        UPDATE pontos_coleta 
        SET nome = ?, endereco = ?, cidade = ?, estado = ?, 
            telefone = ?, horario_funcionamento = ?, tipos_materiais = ?
        WHERE id = ?
    ''', (ponto.nome, ponto.endereco, ponto.cidade, ponto.estado,
          ponto.telefone, ponto.horario_funcionamento, ponto.tipos_materiais,
          ponto.id))
    
    conn.commit()
    conn.close()
    return ponto