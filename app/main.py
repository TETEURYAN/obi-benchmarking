import streamlit as st
from orchestrator import Orchestrator, State
from haystack.dataclasses import ChatMessage

st.set_page_config(page_title="Tutor de IA de Pólya", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
            <style>
            
            /* Estilos para os Cards da Questão (Tema Escuro com Borda Branca) */
            .question-card {
                background-color: transparent;
                margin-bottom: 24px;
                color: #ffffff;
            }
            
            .question-title {
                font-size: 24px;
                font-weight: 700;
                color: #ffffff;
                margin-bottom: 12px;
            }
            
            .section-header {
                font-size: 16px;
                font-weight: 600;
                color: #ffffff;
                margin-bottom: 8px;
                margin-top: 16px;
            }
            
            .content-box {
                padding: 16px; 
                border: 1px solid #ffffff; 
                border-radius: 8px; 
                background-color: #000000; 
                color: #e0e0e0;
                line-height: 1.6;
            }
            
            /* Stepper */
            .stepper-container {
                display: flex;
                justify-content: space-between;
                margin-bottom: 20px;
                gap: 10px;
            }
            .step-box {
                flex: 1;
                text-align: center;
                padding: 10px 5px;
            }
            .step-status {
                font-size: 11px;
                text-transform: uppercase;
                letter-spacing: 1.2px;
                margin-bottom: 4px;
                font-weight: 600;
            }
            .step-title {
                font-size: 16px;
                font-weight: 700;
                color: white;
                margin-bottom: 8px;
            }
            .step-bar {
                height: 6px;
                width: 100%;
                border-radius: 2px;
            }
            </style>
        """, unsafe_allow_html=True)

def render_question_details(question):
    """Renderiza a questão processando o dicionário ou objeto de dados do problema"""
    
    # Auxiliar para obter valores de dict ou objeto de forma segura
    def get_val(obj, key, default="Não especificado."):
        if isinstance(obj, dict):
            return obj.get(key, default)
        return getattr(obj, key, default)

    # Cabeçalho simplificado sem o link de retorno
    title = get_val(question, "title", "Sem título")
    st.markdown(f"## {title}")
    st.divider()

    # 1. Descrição
    st.markdown(f"""
        <div class="question-card">
            <div class="section-header">Descrição</div>
            <div class="content-box">
                {get_val(question, 'description')}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # 2. Formato da Entrada
    st.markdown(f"""
        <div class="question-card">
            <div class="section-header">Formato da Entrada</div>
            <div class="content-box">
                {get_val(question, 'input_format')}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Formato da Saída
    st.markdown(f"""
        <div class="question-card">
            <div class="section-header">Formato da Saída</div>
            <div class="content-box">
                {get_val(question, 'output_format')}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. Exemplos de Entrada e Saída
    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-header">Exemplos de Entrada e Saída</div>', unsafe_allow_html=True)
    
    examples = get_val(question, 'examples', [])
    
    if not examples:
        st.info("Nenhum exemplo disponível.")
    else:
        # Cria a lista de opções para o selectbox
        options = ["Selecione um exemplo..."] + [f"Exemplo {i+1}" for i in range(len(examples))]
        selected_option = st.selectbox("Selecione um exemplo:", options=options, label_visibility="collapsed")
        
        if selected_option != "Selecione um exemplo...":
            # Extrai o índice
            idx = int(selected_option.split(" ")[1]) - 1
            example = examples[idx]
            
            col_in, col_out = st.columns(2)
            with col_in:
                st.markdown("Entrada")
                st.code(get_val(example, "input", ""), language=None)
            with col_out:
                st.markdown("Saída Esperada")
                st.code(get_val(example, "output", ""), language=None)
        else:
            st.caption("Escolha um exemplo acima para visualizar os dados de entrada e saída.")
        
    st.markdown('</div>', unsafe_allow_html=True)
    
def render_phase_stepper(current_state):
    """Renderiza o progresso em barras conforme a imagem fornecida"""
    states = [
        (State.COMPREHENSION, "Compreensão"),
        (State.PLANNING, "Planejamento"),
        (State.IMPLEMENTATION, "Implementação"),
        (State.DONE, "Concluído")
    ]
    
    cols = st.columns(len(states))
    state_list = [s[0] for s in states]
    current_index = state_list.index(current_state) if current_state in state_list else 0
    test_failed = st.session_state.get("test_failed", False)

    for idx, (state, label) in enumerate(states):
        status_text = "PENDENTE"
        color = "#333333" # Cinza escuro para pendente
        
        if current_state == State.DONE or idx < current_index:
            status_text = "CONCLUÍDO"
            color = "#58b368" # Verde (conforme imagem)
        elif idx == current_index:
            status_text = "EM CURSO"
            color = "#3498db" # Azul
            if state == State.IMPLEMENTATION and test_failed:
                status_text = "ERRO DE TESTE"
                color = "#e74c3c" # Vermelho
            elif current_state == State.DONE: # Caso especial para o último passo
                status_text = "CONCLUÍDO"
                color = "#58b368"
        
        cols[idx].markdown(
            f"""
            <div class="step-box">
                <div class="step-status" style="color: {color};">{status_text}</div>
                <div class="step-title">{idx+1}. {label}</div>
                <div class="step-bar" style="background-color: {color};"></div>
            </div>
            """, unsafe_allow_html=True
        )


def render_embedded_chat(height=350, title="Feedback do Tutor", chat_input="Peça uma dica..."):
    """
    Função para renderizar o histórico de chat e o campo de entrada (input)
    dentro de um container específico, utilizando um formulário para evitar
    o comportamento global do st.chat_input.
    """
    st.subheader(title)
    
    feedback_box = st.container(border=True)
    
    with feedback_box:
        # Área de rolagem para o histórico
        chat_history_area = st.container(height=height)
        with chat_history_area:
            # Seleção da fonte de dados baseada no estado do orquestrador
            if orchestrator.state in [State.COMPREHENSION, State.PLANNING]:
                messages = st.session_state.get("messages", [])
                for msg in messages:
                    st.chat_message(msg["role"]).write(msg["content"])
            else:
                for msg in orchestrator.history:
                    role = msg.role.value.lower() if hasattr(msg.role, 'value') else msg.role
                    st.chat_message(role).write(msg.text)

        # Formulário para o input do chat embutido
        with st.form(key=f"chat_form_{orchestrator.state}", clear_on_submit=True):
            col_input, col_btn = st.columns([0.85, 0.15])
            prompt = col_input.text_input(
                "Entrada de chat", 
                label_visibility="collapsed", 
                placeholder=chat_input
            )
            submitted = col_btn.form_submit_button("Enviar", use_container_width=True)

            if submitted and prompt:
                if orchestrator.state in [State.COMPREHENSION, State.PLANNING]:
                    # Fluxo para fases de diálogo (Compreensão/Planejamento)
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    result = orchestrator.handle_message(prompt)
                    st.session_state.messages.append({"role": "assistant", "content": result["feedback"]})
                    
                    if result.get("is_complete"):
                        st.session_state.is_phase_complete = True
                else:
                    # Fluxo para dicas durante a implementação
                    orchestrator.handle_message(prompt)
                
                st.rerun()


# Initialize session state for the orchestrator
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = Orchestrator()

orchestrator = st.session_state.orchestrator

st.set_page_config(page_title="Tutor IA de Pólya", layout="wide")


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
    
    render_question_details(orchestrator.current_question)

    render_phase_stepper(orchestrator.state)
    st.divider()
            
    # Chat interface or Code editor based on state
    if orchestrator.state in [State.COMPREHENSION, State.PLANNING]:
        render_embedded_chat(title="Responda as perguntas do chat abaixo",
                             chat_input="Resonda aqui")

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
        st.info("Leia da entrada padrão e imprima na saída padrão.")

        # Editor
        code = st.text_area(
            "Editor de Código Python",
            value="# Leia a entrada separada por espaço\na, b = map(int, input().split())\nprint(a + b)\n",
            height=350
        )

        # Botão executar
        if st.button("Enviar e Executar Testes"):

            with st.spinner("Avaliando código..."):
                result = orchestrator.evaluate_code(code)
                st.session_state.last_eval = result

                # registrar feedback no histórico
                orchestrator.history.append(
                    ChatMessage.from_assistant(result.get("agent_feedback", ""))
                )

                if result["is_correct"]:
                    orchestrator.state = State.DONE
                    st.session_state.test_failed = False
                else:
                    orchestrator.state = State.IMPLEMENTATION
                    st.session_state.test_failed = True

            st.rerun()


        st.divider()
        
        # -----------------------
        # RESULTADOS DOS TESTES
        # -----------------------

        if "last_eval" in st.session_state:

            eval_res = st.session_state.last_eval

            st.subheader("Resultados dos Testes")

            with st.expander("Ver resultados detalhados"):

                for res in eval_res["test_results"]:

                    st.text(
                        f"Entrada: {res.get('input')} | Status: {res.get('status')}"
                    )

                    if res.get("status") != "Aceito":
                        st.text(f"Esperado: {res.get('expected')}")
                        st.text(f"Obtido: {res.get('actual')}")


        # -----------------------
        # CHAT COM TUTOR
        # -----------------------

        render_embedded_chat(title="Feedback do tutor")

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
            
else:
    st.title("🎓 Tutor IA de Pólya")
    st.markdown("""
                Bem-vindo! Vamos guiá-lo através do processo de resolução de problemas usando o método de quatro etapas de Pólya:
                
                1. **Compreensão**
                2. **Planejamento**
                3. **Implementação**
                4. **Revisão**
                """)
    st.info("Por favor, selecione uma questão na barra lateral para começar.")
