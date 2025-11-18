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

# Criar instância do serviço
service = PontoColetaService()

# Inicializar variáveis de sessão
if 'editar_ponto_id' not in st.session_state:
    st.session_state.editar_ponto_id = None
if 'excluir_ponto_id' not in st.session_state:
    st.session_state.excluir_ponto_id = None

# Header
st.title("🗑️ Sistema de Gestão de Pontos de Coleta")
st.markdown("---")

# Sidebar para navegação
with st.sidebar:
    st.header("Navegação")
    pagina = st.radio("Selecione a página:", ["Cadastrar Ponto", "Listar Pontos"])
    
    st.markdown("---")
    st.info("Sistema completo de CRUD para gerenciamento de pontos de coleta.")

# Página de Cadastro
if pagina == "Cadastrar Ponto":
    st.header("Cadastrar Novo Ponto de Coleta")
    
    # Verificar se está em modo de edição
    if st.session_state.editar_ponto_id:
        ponto = PontoColetaService.buscar_ponto_por_id(st.session_state.editar_ponto_id)
        if ponto:
            st.subheader(f"Editando: {ponto.nome}")
            ponto_atualizado = form_ponto_coleta(ponto)
            
            if ponto_atualizado:
                if PontoColetaService.atualizar_ponto_coleta(ponto_atualizado):
                    st.success("Ponto de coleta atualizado com sucesso!")
                    st.session_state.editar_ponto_id = None
                    st.rerun()
        else:
            st.error("Ponto de coleta não encontrado!")
            st.session_state.editar_ponto_id = None
    else:
        # Formulário de cadastro normal
        novo_ponto = form_ponto_coleta()
        
        if novo_ponto:
            ponto_id = PontoColetaService.criar_ponto_coleta(novo_ponto)
            if ponto_id:
                st.success("Ponto de coleta cadastrado com sucesso!")
                st.balloons()

# Página de Listagem
else:
    st.header("Pontos de Coleta Cadastrados")
    
    # Verificar exclusão
    if st.session_state.excluir_ponto_id:
        ponto = PontoColetaService.buscar_ponto_por_id(st.session_state.excluir_ponto_id)
        if ponto:
            st.warning(f"Tem certeza que deseja excluir o ponto: **{ponto.nome}**?")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("✅ Sim, excluir"):
                    if PontoColetaService.excluir_ponto_coleta(st.session_state.excluir_ponto_id):
                        st.success("Ponto de coleta excluído com sucesso!")
                        st.session_state.excluir_ponto_id = None
                        st.rerun()
            with col2:
                if st.button("❌ Cancelar"):
                    st.session_state.excluir_ponto_id = None
                    st.rerun()
        else:
            st.error("Ponto de coleta não encontrado!")
            st.session_state.excluir_ponto_id = None
    
    # Exibir lista de pontos
    exibir_lista_pontos()

# Footer
st.markdown("---")
st.markdown("Sistema desenvolvido com Streamlit e SQLite")