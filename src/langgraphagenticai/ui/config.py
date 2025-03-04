from configparser import ConfigParser

class Config:
    def __init__(self, config_file="./src/langgraphagenticai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)
    
    def get_llm_model(self):
        return self.config['DEFAULT'].get('LLM_MODEL')
    
    def get_usecase_options(self):
        return self.config['DEFAULT'].get('USECASE_OPTIONS')
    
    def get_groq_model_options(self):
        return self.config['DEFAULT'].get('GROQ_MODEL_OPTIONS')
    
    def get_page_title(self):
        return self.config['DEFAULT'].get('PAGE_TITLE')
    
    def get_sidebar_title(self):
        return self.config['DEFAULT'].get('SIDEBAR_TITLE')
    
    def get_sidebar_placeholder(self):
        return self.config['DEFAULT'].get('SIDEBAR_PLACEHOLDER')
