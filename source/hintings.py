from typing import TypedDict 
from datetime import datetime

    
class LoginDict(TypedDict) :
    
    token: str
    used_last: datetime
    _r_key: int
    maintenance: bool
    