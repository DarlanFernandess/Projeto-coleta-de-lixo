import sqlite3

class PontoColeta:
    def __init__(self, id=None, nome=None, endereco=None, cidade=None, estado=None,
                 telefone=None, horario_funcionamento=None, tipos_materiais=None):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.horario_funcionamento = horario_funcionamento
        self.tipos_materiais = tipos_materiais



def get_connection():
    """
    Retorna uma conexão com o banco de dados SQLite
    """
    return sqlite3.connect('pontos_coleta.db')

def criar_tabela():
    """
    Cria a tabela de pontos de coleta se não existir
    """
    conn = get_connection()
    cursor = conn.cursor()
    
    # Criar tabela com a coluna data_criacao
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pontos_coleta (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            telefone TEXT,
            horario_funcionamento TEXT NOT NULL,
            tipos_materiais TEXT NOT NULL,
            data_criacao TEXT
        )
    ''')
    
    # Verificar se a coluna data_criacao existe, se não, adicionar
    cursor.execute("PRAGMA table_info(pontos_coleta)")
    columns = [column[1] for column in cursor.fetchall()]
    
    if 'data_criacao' not in columns:
        cursor.execute('''
            ALTER TABLE pontos_coleta 
            ADD COLUMN data_criacao TEXT
        ''')
        print("Coluna 'data_criacao' adicionada à tabela!")
    
    conn.commit()
    conn.close()
    print("Tabela 'pontos_coleta' criada/verificada com sucesso!")
