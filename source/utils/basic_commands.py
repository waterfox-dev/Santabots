import json

from source.utils.text import Text


class BasicCommands : 
    
    URL = "assets/commands/basics.json"
    
    def __init__(self) -> None : 
        
        with open(BasicCommands.URL, 'r', encoding='utf8') as json_file : 
            self.json_file = json.load(json_file)
            
    def get(self, key:str, args:list) -> str:
        
        raw = self.json_file[key]
        return Text.get(raw, args)