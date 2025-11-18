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

def criar_tabela():
    """
    Cria a tabela de pontos de coleta se não existir
    """
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
            horario_funcionamento TEXT NOT NULL,
            tipos_materiais TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Tabela 'pontos_coleta' criada/verificada com sucesso!")