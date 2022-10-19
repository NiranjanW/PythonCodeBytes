from typing import Any 
from bs4 import BeautifulSSoup

class XMLConfig:    
    def __init__(self, bs :BeautifulSSoup): 
        self.bs = bs
    
    def get(self,key:str , default :Any =None) -> Any|None :
        value = self.bs.find(key)
        if not value:
            return None
        return value.get_text()

