import streamlit as st
from services.ponto_coleta_service import PontoColetaService
from database.models import PontoColeta

def exibir_lista_pontos(service):
    """Exibe a lista de pontos de coleta usando a instância do service"""
    pontos = service.listar_pontos_coleta()
    
    # Inicializar session_state para cada ponto
    for ponto in pontos:
        if f'editar_{ponto.id}' not in st.session_state:
            st.session_state[f'editar_{ponto.id}'] = False
        if f'excluir_{ponto.id}' not in st.session_state:
            st.session_state[f'excluir_{ponto.id}'] = False
    
    if not pontos:
        st.info("Nenhum ponto de coleta cadastrado ainda.")
        return
    
    for ponto in pontos:
        with st.expander(f"🗑️ {ponto.nome} - {ponto.cidade}/{ponto.estado}", expanded=False):
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
            
            # Botões de Ação
            col_btn1, col_btn2 = st.columns(2)
            
            with col_btn1:
                # Usar on_click para modificar session_state
                if st.button(f"✏️ Editar", key=f"btn_editar_{ponto.id}"):
                    st.session_state[f'editar_{ponto.id}'] = True
                    st.rerun()
            
            with col_btn2:
                if st.button(f"🗑️ Excluir", key=f"btn_excluir_{ponto.id}"):
                    st.session_state[f'excluir_{ponto.id}'] = True
                    st.rerun()
            
            # Modal de Edição - aparece apenas se editar_XX for True
            if st.session_state[f'editar_{ponto.id}']:
                st.subheader(f"✏️ Editando: {ponto.nome}")
                
                with st.form(f"form_editar_{ponto.id}"):
                    nome = st.text_input("Nome do Local*", value=ponto.nome, key=f"nome_{ponto.id}")
                    endereco = st.text_input("Endereço*", value=ponto.endereco, key=f"endereco_{ponto.id}")
                    cidade = st.text_input("Cidade*", value=ponto.cidade, key=f"cidade_{ponto.id}")
                    estado = st.text_input("Estado*", value=ponto.estado, key=f"estado_{ponto.id}")
                    telefone = st.text_input("Telefone", value=ponto.telefone or "", key=f"telefone_{ponto.id}")
                    horario_funcionamento = st.text_input("Horário de Funcionamento*", 
                                                         value=ponto.horario_funcionamento, key=f"horario_{ponto.id}")
                    tipos_materiais = st.text_input("Tipos de Materiais Aceitos*", 
                                                   value=ponto.tipos_materiais, key=f"materiais_{ponto.id}")
                    
                    col_salvar, col_cancelar = st.columns(2)
                    
                    with col_salvar:
                        salvar = st.form_submit_button("💾 Salvar Alterações")
                    
                    with col_cancelar:
                        cancelar = st.form_submit_button("❌ Cancelar")
                    
                    if salvar:
                        if nome and endereco and cidade and estado and horario_funcionamento and tipos_materiais:
                            ponto_atualizado = PontoColeta(
                                id=ponto.id,
                                nome=nome,
                                endereco=endereco,
                                cidade=cidade,
                                estado=estado,
                                telefone=telefone,
                                horario_funcionamento=horario_funcionamento,
                                tipos_materiais=tipos_materiais,
                                data_criacao=ponto.data_criacao
                            )
                            try:
                                service.atualizar_ponto(ponto_atualizado)
                                st.success("✅ Ponto de coleta atualizado com sucesso!")
                                st.session_state[f'editar_{ponto.id}'] = False
                                st.rerun()
                            except Exception as e:
                                st.error(f"❌ Erro ao atualizar ponto: {e}")
                        else:
                            st.error("⚠️ Por favor, preencha todos os campos obrigatórios (*)")
                    
                    if cancelar:
                        st.session_state[f'editar_{ponto.id}'] = False
                        st.rerun()
            
            # Confirmação de Exclusão
            if st.session_state[f'excluir_{ponto.id}']:
                st.warning(f"⚠️ Tem certeza que deseja excluir o ponto '{ponto.nome}'?")
                col_confirmar, col_cancelar_excluir = st.columns(2)
                
                with col_confirmar:
                    if st.button(f"✅ Confirmar Exclusão", key=f"confirmar_excluir_{ponto.id}"):
                        try:
                            service.excluir_ponto(ponto.id)
                            st.success(f"✅ Ponto '{ponto.nome}' excluído com sucesso!")
                            st.session_state[f'excluir_{ponto.id}'] = False
                            st.rerun()
                        except Exception as e:
                            st.error(f"❌ Erro ao excluir ponto: {e}")
                
                with col_cancelar_excluir:
                    if st.button(f"❌ Cancelar", key=f"cancelar_excluir_{ponto.id}"):
                        st.session_state[f'excluir_{ponto.id}'] = False
                        st.rerun()