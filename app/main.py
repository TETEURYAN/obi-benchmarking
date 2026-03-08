import streamlit as st
from orchestrator import Orchestrator, State

# Initialize session state for the orchestrator
if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = Orchestrator()

orchestrator = st.session_state.orchestrator

st.set_page_config(page_title="Pólya AI Tutor", layout="wide")
st.title("🎓 Pólya AI Tutor")
st.markdown("""
Welcome! We'll guide you through the problem-solving process using Pólya's four-step method:
1. **Comprehension** 2. **Planning** 3. **Implementation** 4. **Review**
""")

# Sidebar for question selection
with st.sidebar:
    st.header("Select a Question")
    questions = orchestrator.question_manager.load_questions()
    selected_q_id = st.selectbox("Choose a programming challenge:", options=[q.id for q in questions])
    
    if st.button("Start Question"):
        orchestrator.select_question(selected_q_id)
        intro = orchestrator.start_comprehension()
        st.session_state.messages = [{"role": "assistant", "content": intro}]
        st.session_state.is_phase_complete = False
        st.success(f"Started: {selected_q_id}")

if orchestrator.current_question:
    # Phase Navigation
    cols = st.columns(4)
    for idx, (state, label) in enumerate([
        (State.COMPREHENSION, "1. Comprehension"),
        (State.PLANNING, "2. Planning"),
        (State.IMPLEMENTATION, "3. Implementation"),
        (State.DONE, "4. Done")
    ]):
        if orchestrator.state == state:
            cols[idx].button(label, type="primary", key=f"nav_{state}", disabled=True)
        else:
            cols[idx].button(label, type="secondary", key=f"nav_{state}", disabled=True)

    st.divider()

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

        if prompt := st.chat_input("Ask or respond here..."):
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
            st.success("Great! You seem to have a good understanding of this step.")
            if st.button("Proceed to Next Phase →"):
                orchestrator.next_phase()
                if orchestrator.state == State.PLANNING:
                    intro = orchestrator.start_planning()
                    st.session_state.messages = [{"role": "assistant", "content": intro}]
                else:
                    st.session_state.messages = []
                st.session_state.is_phase_complete = False
                st.rerun()

    elif orchestrator.state == State.IMPLEMENTATION:
        st.info("Write your implementation below.")
        # ... (rest of implementation code same as before)
        code = st.text_area("Python Code Editor", value="def sum_two_numbers(a, b):\n    return a + b", height=300)
        
        if st.button("Submit & Run Tests"):
            # Call judge
            results = orchestrator.judge.evaluate(
                code, 
                language_id=71, # Python 3
                test_cases=[tc.model_dump() for tc in orchestrator.current_question.test_cases]
            )
            st.write("Results:", results)
            
            if all(r["status"] == "Accepted" for r in results):
                st.success("All tests passed!")
                orchestrator.next_phase()
                st.rerun()
            else:
                st.error("Some tests failed. Ask the Implementation Agent for help!")

    elif orchestrator.state == State.DONE:
        st.balloons()
        st.success("Congratulations! You've solved the problem using the Pólya method.")
        if st.button("Try another question"):
            orchestrator.state = State.SELECTING_QUESTION
            orchestrator.current_question = None
            st.session_state.messages = []
            st.rerun()

else:
    st.info("Please select a question from the sidebar to begin.")
