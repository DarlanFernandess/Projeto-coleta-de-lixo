import streamlit as st
from services.ponto_coleta_service import PontoColetaService

def exibir_lista_pontos():
    service = PontoColetaService()  # Criar instância
    pontos = service.listar_pontos_coleta()  # Chamar método da instância
    
    
    if not pontos:
        st.info("Nenhum ponto de coleta cadastrado.")
        return
    
    for ponto in pontos:
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            
            with col1:
                st.subheader(ponto.nome)
                st.write(f"**Endereço:** {ponto.endereco}, {ponto.cidade} - {ponto.estado}")
                if ponto.telefone:
                    st.write(f"**Telefone:** {ponto.telefone}")
                if ponto.horario_funcionamento:
                    st.write(f"**Horário:** {ponto.horario_funcionamento}")
                if ponto.tipos_materiais:
                    st.write(f"**Materiais aceitos:** {ponto.tipos_materiais}")
            
            with col2:
                if st.button("✏️ Editar", key=f"edit_{ponto.id}"):
                    st.session_state.editar_ponto_id = ponto.id
                    st.rerun()
            
            with col3:
                if st.button("🗑️ Excluir", key=f"del_{ponto.id}"):
                    st.session_state.excluir_ponto_id = ponto.id
                    st.rerun()
            
            st.divider()