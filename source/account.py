import json


class Account:

    @classmethod
    def new_account(self, id: int, name: str) -> None:

        with open('assets/account.json', 'r', encoding='utf8') as r_file:
            r_file = json.load(r_file)

        r_file[id] = {
            "name":  name,
            "message":
            {
                "to": None,
                "content": None
            }
        }

        with open('assets/account.json', 'w', encoding='utf8') as w_file:
            json.dump(r_file, w_file)

    @classmethod
    def get_account(self, id: int) -> None:

        with open('assets/account.json', 'r', encoding='utf8') as r_file:
            r_file = json.load(r_file)

        return r_file[id]

    @classmethod
    def get_receiver(self, id: int) -> tuple[int, str]:

        with open('assets/account.json', 'r', encoding='utf8') as r_file:
            r_file = json.load(r_file)

        return (r_file[id]['message']['to'], r_file[r_file[id]['message']['to']]['name'])

    @classmethod
    def write_message(self, id: int, message: str) -> None : 
        with open('assets/account.json', 'r', encoding='utf8') as r_file:
            r_file = json.load(r_file)

        r_file[id]['message']['content'] = message 

        with open('assets/account.json', 'w', encoding='utf8') as w_file:
            json.dump(r_file, w_file)

    @classmethod 
    def get_message(self, id) -> str : 
        with open('assets/account.json', 'r', encoding='utf8') as r_file:
            r_file = json.load(r_file)

        return r_file[id]['message']['content']
    
    @classmethod 
    def get_secret_message(self, id) -> str : 
        with open('assets/account.json', 'r', encoding='utf8') as r_file:
            r_file = dict(json.load(r_file))
        
        for key, value in r_file.items() : 
            if value['message']['to'] == id : 
                return value['message']['content']

    @classmethod 
    def get_members(self): 
        with open('assets/account.json', 'r', encoding='utf8') as r_file:
            r_file = dict(json.load(r_file))
        
        l = []

        for element in r_file.keys() :
            l.append(r_file[element]['name'])
        
        return l