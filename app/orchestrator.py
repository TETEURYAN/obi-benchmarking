import logging
from enum import Enum
from typing import Optional, Dict, Any, List
from question_manager import Question, QuestionManager
from agents.comprehension import ComprehensionAgent
from agents.planning import PlanningAgent
from agents.implementation import ImplementationAgent
from judge import Judge
from haystack.dataclasses import ChatMessage

logger = logging.getLogger(__name__)

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
        logger.info("Orchestrator initialized.")

    def select_question(self, question_id: str):
        logger.info(f"Selecting question: {question_id}")
        self.current_question = self.question_manager.get_question_by_id(question_id)
        if self.current_question:
            self.state = State.COMPREHENSION
            self.history = []
            self.comprehension_summary = ""
            self.plan_summary = ""
            logger.info(f"Question '{self.current_question.title}' selected. State moved to COMPREHENSION.")
        else:
            logger.warning(f"Question ID '{question_id}' not found.")
        return self.current_question

    def start_comprehension(self) -> str:
        """Generates the first message to start the comprehension phase."""
        if not self.current_question:
            return "Please select a question first."
        
        intro_message = f"Hello! I'm here to help you understand the '{self.current_question.title}' problem. Can you tell me what you think this problem is asking you to do in your own words?"
        self.history.append(ChatMessage.from_assistant(intro_message))
        logger.info("Comprehension phase started.")
        return intro_message

    def start_planning(self) -> str:
        """Generates the first message to start the planning phase."""
        if not self.current_question:
            return "Please select a question first."
        
        intro_message = f"Great job understanding the problem! Now, let's devise a plan for the '{self.current_question.title}' challenge. How would you solve this step-by-step? (Remember, no code for now, just the logic!)"
        self.history.append(ChatMessage.from_assistant(intro_message))
        logger.info("Planning phase started.")
        return intro_message

    def handle_message(self, message: str) -> Dict[str, Any]:
        logger.info(f"Handling message in state {self.state.value}")
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
                logger.info("Comprehension marked as COMPLETE by agent.")
            
            return result
        
        elif self.state == State.PLANNING:
            result = self.planning_agent.run(
                self.current_question.description,
                self.comprehension_summary,
                message,
                self.history
            )
            
            # Update history
            self.history.append(ChatMessage.from_user(message))
            self.history.append(ChatMessage.from_assistant(result["feedback"]))
            
            if result.get("is_complete"):
                self.plan_summary = result.get("plan", "")
                logger.info("Planning marked as COMPLETE by agent.")
            
            return result
            
        elif self.state == State.IMPLEMENTATION:
            # Simple wrapper for chat in implementation phase
            self.history.append(ChatMessage.from_user(message))
            result = self.implementation_agent.run(
                self.current_question.description,
                self.plan_summary,
                "", # No code for a pure chat message
                "Student is asking a question.",
                message,
                self.history
            )
            self.history.append(ChatMessage.from_assistant(result["feedback"]))
            return result
            
        return {"feedback": "Please select a question first.", "is_complete": False}

    def evaluate_code(self, code: str) -> Dict[str, Any]:
        """Runs the code through the judge and then through the implementation agent for feedback."""
        logger.info("Starting code evaluation.")
        test_results = self.judge.evaluate(
            code,
            language="python",
            test_cases=[tc.model_dump() for tc in self.current_question.test_cases]
        )
        
        # Format results for the agent
        results_str = ""
        all_passed = True
        for res in test_results:
            status = res.get("status")
            if status != "Accepted":
                all_passed = False
            results_str += f"Input: {res.get('input')}, Expected: {res.get('expected')}, Actual: {res.get('actual')}, Status: {status}\n"

        logger.info(f"Tests execution finished. All passed: {all_passed}")

        # Get feedback from agent
        agent_result = self.implementation_agent.run(
            self.current_question.description,
            self.plan_summary,
            code,
            results_str,
            "User submitted code for evaluation."
        )
        
        if all_passed:
            agent_result["is_correct"] = True
            logger.info("Code evaluation: CORRECT")
        else:
            logger.info("Code evaluation: INCORRECT")
            
        return {
            "test_results": test_results,
            "agent_feedback": agent_result["feedback"],
            "is_correct": agent_result["is_correct"]
        }

    def next_phase(self):
        old_state = self.state
        if self.state == State.COMPREHENSION:
            self.state = State.PLANNING
            self.history = [] 
        elif self.state == State.PLANNING:
            self.state = State.IMPLEMENTATION
            self.history = []
        elif self.state == State.IMPLEMENTATION:
            self.state = State.DONE
        logger.info(f"Phase transition: {old_state.value} -> {self.state.value}")
