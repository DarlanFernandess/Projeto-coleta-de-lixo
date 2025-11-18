🗑️ Sistema de Coleta de Lixo
Um sistema web desenvolvido em Python com Streamlit para gerenciamento de pontos de coleta de materiais recicláveis.

📋 Sobre o Projeto
Este sistema permite o cadastro, listagem, edição e exclusão de pontos de coleta de lixo reciclável, facilitando o gerenciamento de locais onde a população pode descartar corretamente diferentes tipos de materiais.

✨ Funcionalidades
✅ Cadastro de Pontos de Coleta - Formulário completo para cadastrar novos pontos

✅ Listagem de Pontos - Visualização organizada de todos os pontos cadastrados

✅ Edição de Pontos - Modificação de informações dos pontos existentes

✅ Exclusão de Pontos - Remoção segura com confirmação

✅ Busca e Filtros - Facilidade para encontrar pontos específicos

✅ Interface Responsiva - Design adaptável para diferentes dispositivos

🛠️ Tecnologias Utilizadas
Python 3.8+ - Linguagem de programação

Streamlit - Framework para aplicações web

SQLite - Banco de dados relacional

Pandas - Manipulação de dados (se necessário)

📦 Estrutura do Projeto
text
projeto-coleta-de-lixo/
├── app.py                          # Aplicação principal
├── requirements.txt                # Dependências do projeto
├── database/
│   ├── __init__.py
│   ├── database.py                 # Configuração do banco de dados
│   └── models.py                   # Modelos de dados
├── services/
│   ├── __init__.py
│   └── ponto_coleta_service.py     # Lógica de negócio
└── components/
    ├── __init__.py
    ├── form_cadastro.py            # Componente do formulário
    └── lista_pontos.py             # Componente da lista
🚀 Como Executar o Projeto
Pré-requisitos
Python 3.8 ou superior

pip (gerenciador de pacotes do Python)

Instalação
Clone o repositório:

bash
git clone https://github.com/seu-usuario/projeto-coleta-de-lixo.git
cd projeto-coleta-de-lixo
Crie um ambiente virtual (recomendado):

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Execute a aplicação:

bash
streamlit run app.py
Acesse no navegador:

text
http://localhost:8501
📊 Como Usar
Cadastrar um Novo Ponto de Coleta
Acesse a opção "Cadastrar Ponto de Coleta" no menu lateral

Preencha todos os campos obrigatórios (*)

Clique em "Cadastrar Ponto de Coleta"

Gerenciar Pontos Existentes
Acesse "Listar Pontos de Coleta" no menu lateral

Use os botões "Editar" ou "Excluir" em cada ponto

Para editar: modifique os dados e clique em "Salvar Alterações"

Para excluir: confirme a exclusão no modal de confirmação

🗃️ Modelo de Dados
O sistema armazena as seguintes informações para cada ponto de coleta:

Campo	Tipo	Obrigatório	Descrição
id	Integer	✅	Identificador único
nome	Text	✅	Nome do local
endereco	Text	✅	Endereço completo
cidade	Text	✅	Cidade
estado	Text	✅	Estado
telefone	Text	✅	Telefone para contato
horario_funcionamento	Text	✅	Horário de funcionamento
tipos_materiais	Text	✅	Tipos de materiais aceitos
data_criacao	Timestamp	✅	Data de cadastro
🌐 Deploy
Streamlit Cloud (Recomendado)
Faça upload do projeto para o GitHub

Acesse share.streamlit.io

Conecte com sua conta GitHub

Selecione o repositório e branch

Configure o arquivo principal como app.py

Clique em Deploy

Outras Plataformas
Heroku - Com buildpack do Python

Railway - Deploy simplificado

AWS/Azure - Com configuração de containers

🤝 Contribuindo
Contribuições são sempre bem-vindas! Para contribuir:

Fork o projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📝 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

👨‍💻 Desenvolvedor
Darlan Fernandes

GitHub: @darlanfernandess

Email: seu-email@exemplo.com

🐛 Reportar Bugs
Encontrou um bug? Por favor, abra uma issue descrevendo o problema.

🔄 Histórico de Versões
v1.0.0 - Versão inicial com CRUD completo

v1.1.0 - Adicionado funcionalidade de edição

v1.2.0 - Melhorias na interface e experiência do usuário

⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!

