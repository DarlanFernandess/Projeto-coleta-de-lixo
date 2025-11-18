class PontoColeta:
    def __init__(self, id=None, nome=None, endereco=None, cidade=None, estado=None,
                 telefone=None, horario_funcionamento=None, tipos_materiais=None, 
                 data_criacao=None):
        self.id = id
        self.nome = nome
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.telefone = telefone
        self.horario_funcionamento = horario_funcionamento
        self.tipos_materiais = tipos_materiais
        self.data_criacao = data_criacao
    
    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'endereco': self.endereco,
            'cidade': self.cidade,
            'estado': self.estado,
            'telefone': self.telefone,
            'horario_funcionamento': self.horario_funcionamento,
            'tipos_materiais': self.tipos_materiais,
            'data_criacao': self.data_criacao
        }
    
    @classmethod
    def from_dict(cls, data):
        """Cria um objeto PontoColeta a partir de um dicionário"""
        return cls(
            id=data.get('id'),
            nome=data.get('nome'),
            endereco=data.get('endereco'),
            cidade=data.get('cidade'),
            estado=data.get('estado'),
            telefone=data.get('telefone'),
            horario_funcionamento=data.get('horario_funcionamento'),
            tipos_materiais=data.get('tipos_materiais'),
            data_criacao=data.get('data_criacao')
        )