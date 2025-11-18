import streamlit as st
from database.database import criar_tabela
from services.ponto_coleta_service import PontoColetaService
from components.form_cadastro import form_ponto_coleta
from components.lista_pontos import exibir_lista_pontos

# Configuração da página
st.set_page_config(
    page_title="Sistema de Pontos de Coleta",
    page_icon="🗑️",
    layout="wide"
)

# Inicializar banco de dados
criar_tabela()

# Criar instância do serviço (ADICIONE ESTA LINHA)
service = PontoColetaService()

# Título da aplicação
st.title("🗑️ Sistema de Coleta de Lixo")
st.markdown("---")

# Menu lateral
menu = st.sidebar.selectbox(
    "Menu",
    ["Cadastrar Ponto de Coleta", "Listar Pontos de Coleta"]
)

if menu == "Cadastrar Ponto de Coleta":
    st.header("📝 Cadastrar Novo Ponto de Coleta")
    
    # Usar a instância 'service' em vez da classe
    novo_ponto = form_ponto_coleta()
    if novo_ponto:
        try:
            # CORRIGIDO: usar service.criar_ponto_coleta() em vez de PontoColetaService.criar_ponto_coleta()
            ponto_salvo = service.criar_ponto_coleta(novo_ponto)
            st.success(f"Ponto de coleta '{ponto_salvo.nome}' cadastrado com sucesso! ID: {ponto_salvo.id}")
        except Exception as e:
            st.error(f"Erro ao cadastrar ponto: {e}")

elif menu == "Listar Pontos de Coleta":
    st.header("📋 Pontos de Coleta Cadastrados")
    
    # CORRIGIDO: passar a instância do service para a função
    exibir_lista_pontos(service)