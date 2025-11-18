import streamlit as st
from database.models import PontoColeta

def form_ponto_coleta():
    """Formulário para cadastrar ponto de coleta"""
    with st.form("form_ponto_coleta"):
        st.subheader("Novo Ponto de Coleta")
        
        nome = st.text_input("Nome do Local*")
        endereco = st.text_input("Endereço*")
        cidade = st.text_input("Cidade*")
        estado = st.text_input("Estado*")
        telefone = st.text_input("Telefone")
        horario_funcionamento = st.text_input("Horário de Funcionamento*")
        tipos_materiais = st.text_input("Tipos de Materiais Aceitos*")
        
        submitted = st.form_submit_button("Cadastrar Ponto de Coleta")
        
        if submitted:
            if nome and endereco and cidade and estado and horario_funcionamento and tipos_materiais:
                return PontoColeta(
                    nome=nome,
                    endereco=endereco,
                    cidade=cidade,
                    estado=estado,
                    telefone=telefone,
                    horario_funcionamento=horario_funcionamento,
                    tipos_materiais=tipos_materiais
                )
            else:
                st.error("Por favor, preencha todos os campos obrigatórios (*)")
                return None
    
    return None