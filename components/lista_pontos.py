import streamlit as st  # ADICIONE ESTA LINHA
from services.ponto_coleta_service import PontoColetaService

def exibir_lista_pontos(service):
    """Exibe a lista de pontos de coleta usando a instância do service"""
    pontos = service.listar_pontos_coleta()
    
    if not pontos:
        st.info("Nenhum ponto de coleta cadastrado ainda.")
        return
    
    for ponto in pontos:
        with st.expander(f"🗑️ {ponto.nome} - {ponto.cidade}/{ponto.estado}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(f"**Endereço:** {ponto.endereco}")
                st.write(f"**Cidade:** {ponto.cidade}")
                st.write(f"**Estado:** {ponto.estado}")
                st.write(f"**Telefone:** {ponto.telefone}")
            
            with col2:
                st.write(f"**Horário:** {ponto.horario_funcionamento}")
                st.write(f"**Materiais:** {ponto.tipos_materiais}")
                if ponto.data_criacao:
                    st.write(f"**Cadastrado em:** {ponto.data_criacao}")
            
            # Botão para excluir
            if st.button(f"Excluir {ponto.nome}", key=ponto.id):
                try:
                    service.excluir_ponto(ponto.id)
                    st.success(f"Ponto '{ponto.nome}' excluído com sucesso!")
                    st.rerun()
                except Exception as e:
                    st.error(f"Erro ao excluir ponto: {e}")