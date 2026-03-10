import streamlit as st
from orchestrator import Orchestrator, State

# Initialize session state for the orchestrator
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = Orchestrator()

orchestrator = st.session_state.orchestrator

st.set_page_config(page_title="Tutor IA de Pólya", layout="wide")
st.title("🎓 Tutor IA de Pólya")
st.markdown("""
Bem-vindo! Vamos guiá-lo através do processo de resolução de problemas usando o método de quatro etapas de Pólya:
1. **Compreensão**\n2. **Planejamento**\n3. **Implementação**\n4. **Revisão**
""")

# Sidebar for question selection and debug tools
with st.sidebar:
    st.header("Selecionar uma Questão")
    questions = orchestrator.question_manager.load_questions()
    selected_q_id = st.selectbox("Escolha um desafio de programação:", options=[q.id for q in questions])
    
    if st.button("Iniciar Questão"):
        orchestrator.select_question(selected_q_id)
        intro = orchestrator.start_comprehension()
        st.session_state.messages = [{"role": "assistant", "content": intro}]
        st.session_state.is_phase_complete = False
        st.success(f"Iniciado: {selected_q_id}")

    st.divider()
    st.header("Ferramentas de Depuração")
    if st.button("⏭️ Pular para Próxima Fase"):
        orchestrator.next_phase()
        if orchestrator.state == State.PLANNING:
            intro = orchestrator.start_planning()
            st.session_state.messages = [{"role": "assistant", "content": intro}]
        else:
            st.session_state.messages = []
        st.session_state.is_phase_complete = False
        st.rerun()

if orchestrator.current_question:

    # Step-by-step content
    st.subheader(f"{orchestrator.current_question.title}")
    st.write(orchestrator.current_question.description)

    # Chat interface or Code editor based on state
    if orchestrator.state in [State.COMPREHENSION, State.PLANNING]:
        chat_container = st.container(height=400)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        for msg in st.session_state.messages:
            chat_container.chat_message(msg["role"]).write(msg["content"])

        if prompt := st.chat_input("Pergunte ou responda aqui..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            chat_container.chat_message("user").write(prompt)
            
            # Orchestrator handles the logic
            result = orchestrator.handle_message(prompt)
            response = result["feedback"]
            
            st.session_state.messages.append({"role": "assistant", "content": response})
            chat_container.chat_message("assistant").write(response)
            
            if result.get("is_complete"):
                st.session_state.is_phase_complete = True
                st.rerun()

        if st.session_state.get("is_phase_complete"):
            st.success("Ótimo! Você parece ter uma boa compreensão desta etapa.")
            if st.button("Prosseguir para Próxima Fase →"):
                orchestrator.next_phase()
                if orchestrator.state == State.PLANNING:
                    intro = orchestrator.start_planning()
                    st.session_state.messages = [{"role": "assistant", "content": intro}]
                else:
                    st.session_state.messages = []
                st.session_state.is_phase_complete = False
                st.rerun()
        
    elif orchestrator.state == State.IMPLEMENTATION:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.info("Leia da entrada padrão e imprima na saída padrão.")
            code = st.text_area("Editor de Código Python", value="# Leia a entrada separada por espaço\na, b = map(int, input().split())\nprint(a + b)\n", height=400)
            
            if st.button("Enviar e Executar Testes"):
                with st.spinner("Avaliando código..."):
                    result = orchestrator.evaluate_code(code)
                    st.session_state.last_eval = result

                    if result["is_correct"]:
                        orchestrator.state = State.DONE
                        st.session_state.test_failed = False
                    else:
                        orchestrator.state = State.IMPLEMENTATION
                        st.session_state.test_failed = True

                st.rerun()
                
        with col2:
            st.subheader("Feedback do Tutor")
            chat_container = st.container(height=250)
            
            # Show chat history for implementation phase
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            for msg in st.session_state.messages:
                chat_container.chat_message(msg["role"]).write(msg["content"])

            # If there was a last evaluation, show the feedback as an assistant message
            if "last_eval" in st.session_state:
                eval_res = st.session_state.last_eval
                chat_container.chat_message("assistant").write(eval_res["agent_feedback"])
                
                with st.expander("Ver Resultados Detalhados dos Testes"):
                    for res in eval_res["test_results"]:
                        st.text(f"Entrada: {res.get('input')} | Status: {res.get('status')}")
                        if res.get("status") != "Aceito":
                            st.text(f"  Esperado: {res.get('expected')}")
                            st.text(f"  Atual: {res.get('actual')}")

            if prompt := st.chat_input("Peça uma dica..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                # No code for simple chat
                res = orchestrator.handle_message(prompt)
                st.session_state.messages.append({"role": "assistant", "content": res["feedback"]})
                st.rerun()

        if st.session_state.get("is_phase_complete"):
            st.success("Parabéns! Seu código passou em todos os testes e corresponde ao plano.")
            if st.button("Finalizar Solução"):
                orchestrator.next_phase()
                st.session_state.is_phase_complete = False
                st.session_state.messages = []
                if "last_eval" in st.session_state:
                    del st.session_state.last_eval
                st.rerun()

    elif orchestrator.state == State.DONE:
        st.balloons()
        st.success("Parabéns! Você resolveu o problema usando o método de Pólya.")
        if st.button("Tentar outra questão"):
            orchestrator.state = State.SELECTING_QUESTION
            orchestrator.current_question = None

            # limpar estados da sessão
            for key in ["messages", "last_eval", "is_phase_complete", "test_failed"]:
                if key in st.session_state:
                    del st.session_state[key]

            st.rerun()

    states = [
        (State.COMPREHENSION, "Compreensão"),
        (State.PLANNING, "Planejamento"),
        (State.IMPLEMENTATION, "Implementação"),
        (State.DONE, "Concluído")
    ]

    cols = st.columns(len(states))

    state_list = [s[0] for s in states]

    if orchestrator.state not in state_list:
        st.stop()

    current_index = state_list.index(orchestrator.state)
    states = [
        (State.COMPREHENSION, "Compreensão"),
        (State.PLANNING, "Planejamento"),
        (State.IMPLEMENTATION, "Implementação"),
        (State.DONE, "Concluído")
    ]

    cols = st.columns(len(states))

    current_index = [s[0] for s in states].index(orchestrator.state)
    test_failed = st.session_state.get("test_failed", False)

    for idx, (state, label) in enumerate(states):

        # Caso final correto
        if orchestrator.state == State.DONE:
            display = f"✅ {idx+1}. {label}"
            button_type = "secondary"

        # Caso erro nos testes
        elif state == State.DONE and test_failed:
            display = f"❌ {idx+1}. {label}"
            button_type = "secondary"

        elif idx < current_index:
            display = f"✅ {idx+1}. {label}"
            button_type = "secondary"

        elif idx == current_index:
            display = f"🔵 {idx+1}. {label}"
            button_type = "primary"

        else:
            display = f"⚪ {idx+1}. {label}"
            button_type = "secondary"

        cols[idx].button(
            display,
            key=f"nav_{state}",
            type=button_type,
            disabled=True
        )

    st.divider()
            
else:
    st.info("Por favor, selecione uma questão na barra lateral para começar.")
