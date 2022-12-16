from datetime import datetime

import random
import json 


class Login :
    
    @classmethod
    def load(self, maintenance:bool):
        
        with open('private/login.json', 'r', encoding='utf8') as file :
            self.logins = str(json.load(file)['token'])
        
        _r_key = random.randint(0, 9223372036854775807) 
        return self.logins
       
 
class Settings : 
    
    def __init__(self) : 
        self.load()
    
    def change_functionnalities(self, name, value) : 

        with open('private/settings.json', 'r', encoding='utf8') as file :
            
            file = json.load(file)

        file['functionnalities'][name] = value
        
        with open('private/settings.json', 'w', encoding='utf8') as w_file :

            json.dump(file, w_file)
        self.load()

    def load(self) :
        
        with open('private/settings.json', 'r', encoding='utf8') as file :
            
            file = json.load(file)
            
            for key, value in dict(file).items() :
                print(key, value)
                self.__setattr__(key, value) 