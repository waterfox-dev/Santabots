from datetime import datetime

import sqlite3


class Database : 
    
    def __init__(self) -> None : 
        
        self._con = sqlite3.connect("assets/database/quotebot.db")
        self._cur = self._con.cursor()
        
    def execute(self, query: str) -> list[tuple] :
       
        res = self._cur.execute(query)
        self._con.commit()
        
        return res.fetchall()
   
    def new_guild(self, id: int, name: str, join_date: datetime, comment: str) -> list[tuple] :
        
        res = self._cur.execute(f"INSERT INTO guild VALUES ({id}, {name}, {join_date}, {comment})")
        self._con.commit()
        
        return res.fetchall()
    
    def new_quote_list(self, id: int, guild_id: int, name: str) -> list[tuple] :
        
        res = self._cur.execute(f"INSERT INTO quote_list VALUES ({id}, {guild_id}, {name})")
        self._con.commit()
        
        return res.fetchall()
    
    