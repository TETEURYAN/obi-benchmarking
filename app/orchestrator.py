from enum import Enum
from typing import Optional, Dict, Any, List
from question_manager import Question, QuestionManager
from agents.comprehension import ComprehensionAgent
from agents.planning import PlanningAgent
from agents.implementation import ImplementationAgent
from judge import Judge
from haystack.dataclasses import ChatMessage

class State(Enum):
    SELECTING_QUESTION = "SELECTING_QUESTION"
    COMPREHENSION = "COMPREHENSION"
    PLANNING = "PLANNING"
    IMPLEMENTATION = "IMPLEMENTATION"
    DONE = "DONE"

class Orchestrator:
    def __init__(self):
        self.state = State.SELECTING_QUESTION
        self.current_question: Optional[Question] = None
        self.question_manager = QuestionManager()
        self.judge = Judge()
        
        # Agents
        self.comprehension_agent = ComprehensionAgent()
        self.planning_agent = PlanningAgent()
        self.implementation_agent = ImplementationAgent()
        
        # Memory/Context
        self.comprehension_summary = ""
        self.plan_summary = ""
        self.history: List[ChatMessage] = []

    def select_question(self, question_id: str):
        self.current_question = self.question_manager.get_question_by_id(question_id)
        if self.current_question:
            self.state = State.COMPREHENSION
            self.history = []
            self.comprehension_summary = ""
            self.plan_summary = ""
        return self.current_question

    def start_comprehension(self) -> str:
        """Generates the first message to start the comprehension phase."""
        if not self.current_question:
            return "Please select a question first."
        
        # Initial prompt to the agent to introduce the problem
        intro_message = f"Hello! I'm here to help you understand the '{self.current_question.title}' problem. Can you tell me what you think this problem is asking you to do in your own words?"
        self.history.append(ChatMessage.from_assistant(intro_message))
        return intro_message

    def handle_message(self, message: str) -> Dict[str, Any]:
        if self.state == State.COMPREHENSION:
            result = self.comprehension_agent.run(
                self.current_question.description,
                ", ".join(self.current_question.constraints),
                message,
                self.history
            )
            
            # Update history
            self.history.append(ChatMessage.from_user(message))
            self.history.append(ChatMessage.from_assistant(result["feedback"]))
            
            if result.get("is_complete"):
                self.comprehension_summary = result.get("summary", "")
                # We don't automatically transition here so the UI can show the final feedback
                # and a "Next" button.
            
            return result
        
        elif self.state == State.PLANNING:
            # Placeholder for planning logic
            self.history.append(ChatMessage.from_user(message))
            result = self.planning_agent.run(
                self.current_question.description,
                self.comprehension_summary,
                message
            )
            self.history.append(ChatMessage.from_assistant(result["reply"]))
            return {"feedback": result["reply"], "is_complete": False}
            
        elif self.state == State.IMPLEMENTATION:
            return {"feedback": "Implement your solution now.", "is_complete": False}
            
        return {"feedback": "Please select a question first.", "is_complete": False}

    def next_phase(self):
        if self.state == State.COMPREHENSION:
            self.state = State.PLANNING
            self.history = [] # Clear history for next phase or keep it? 
        elif self.state == State.PLANNING:
            self.state = State.IMPLEMENTATION
            self.history = []
        elif self.state == State.IMPLEMENTATION:
            self.state = State.DONE
