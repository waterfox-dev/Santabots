import random 
import json 

class Giver :

    @classmethod 
    def distribute(self) -> None : 
        
        with open('assets/account.json', 'r', encoding='utf8') as r_file : 
            r_file = dict(json.load(r_file))
        
        id_list = []        
        for element in r_file.keys() :
            id_list.append(element)        
        target_list = id_list.copy() 

        for element in id_list :      
            run = True 
            while run :             
                target = random.choice(target_list)
                if target != element : 
                    target_list.remove(target)
                    run = False
            
            r_file[element]["message"]["to"] = target

        with open('assets/account.json', 'w', encoding='utf8') as w_file : 
            json.dump(r_file, w_file)
