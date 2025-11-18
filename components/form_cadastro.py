import streamlit as st
from database.models import PontoColeta

def form_ponto_coleta(ponto_coleta=None):
    """Componente de formulário para cadastrar/editar ponto de coleta"""
    
    # Valores padrão para novo cadastro ou valores existentes para edição
    if ponto_coleta:
        nome = ponto_coleta.nome
        endereco = ponto_coleta.endereco
        cidade = ponto_coleta.cidade
        estado = ponto_coleta.estado
        telefone = ponto_coleta.telefone
        horario = ponto_coleta.horario_funcionamento
        materiais = ponto_coleta.tipos_materiais
    else:
        nome = ""
        endereco = ""
        cidade = ""
        estado = ""
        telefone = ""
        horario = ""
        materiais = ""
    
    with st.form(key="form_ponto_coleta", clear_on_submit=not ponto_coleta):
        col1, col2 = st.columns(2)
        
        with col1:
            nome_input = st.text_input("Nome do Ponto de Coleta*", value=nome)
            endereco_input = st.text_input("Endereço*", value=endereco)
            cidade_input = st.text_input("Cidade*", value=cidade)
            estado_input = st.selectbox(
                "Estado*",
                ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", 
                 "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", 
                 "RS", "RO", "RR", "SC", "SP", "SE", "TO"],
                index=24 if estado == "SP" else 0
            )
        
        with col2:
            telefone_input = st.text_input("Telefone", value=telefone)
            horario_input = st.text_input("Horário de Funcionamento", value=horario)
            materiais_input = st.text_area(
                "Tipos de Materiais Aceitos", 
                value=materiais,
                placeholder="Ex: Papel, Plástico, Vidro, Metal..."
            )
        
        submitted = st.form_submit_button("Salvar Ponto de Coleta")
        
        if submitted:
            if not nome_input or not endereco_input or not cidade_input:
                st.error("Por favor, preencha os campos obrigatórios (*)")
                return None
            else:
                return PontoColeta(
                    id=ponto_coleta.id if ponto_coleta else None,
                    nome=nome_input,
                    endereco=endereco_input,
                    cidade=cidade_input,
                    estado=estado_input,
                    telefone=telefone_input,
                    horario_funcionamento=horario_input,
                    tipos_materiais=materiais_input
                )
    
    return None