class JudgeService:
    
    def __init__ (self, language: str = "None"):
        self.__language = language
        
        if language == "python":
            self.__format_file_code = "py"

    def execute(code: str):
        pass