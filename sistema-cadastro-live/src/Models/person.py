class Person():
    def __init__(self,idx:str,name:str,idade:int,cpf:str) -> None:
        self.idx = idx
        self.name = name
        self.idade = idade
        self.__cpf = cpf 
        
    @property
    def showdocument(self):
        return self.__cpf 
    @showdocument.setter
    def showdocument(self,dados):
        self.__cpf = dados
        
    def serialize(self):
        return {"id": self.idx,
                    "name":self.name,
                        "idade":self.idade,
                            "cpf": self.showdocument}

            
            
        
        
    