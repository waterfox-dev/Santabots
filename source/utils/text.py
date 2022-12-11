import json 

class Text :
    
    @classmethod
    def get(self, text: str, args_array) -> str:
        
        raw_text = str(text)
        str_ct = raw_text.count('{str')
        int_ct = raw_text.count('{int')
        cmpt = 0
        
        for i in range(str_ct):
            r_text = '{str.'+str(i+1)+'}'
      
            
            if type(args_array[cmpt]) != str : 
                raise TypeError(f"{type(args_array[cmpt])}({args_array[cmpt]}) is not a str")
    
            raw_text = raw_text.replace(r_text, args_array[cmpt])
            cmpt += 1
        
        for i in range(int_ct):
            r_text = '{int.'+str(i+1)+'}'
            if type(args_array[cmpt]) != int :
                raise TypeError
            
            raw_text = raw_text.replace(r_text, str(args_array[cmpt]))
            cmpt += 1
        
        return raw_text        
        