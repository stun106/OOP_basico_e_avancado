from Models.person import Person
from Db.base import Database
class ReqController():
    def __init__(self) -> None:
        self.base = Database()
    
    def insertDados(self, nome,idade,cpf)-> None:
        idx = len(self.base.db) + 1
        set_cep = Person.showdocument = cpf
        user = Person.serialize(Person(idx,nome,idade,set_cep))
        self.base.db.append(user)
        print("dados inseridos com sucesso!")
    
    def selectForName(self,nome:str)-> dict:
        # search = list(filter(lambda obj: nome == obj["name"],self.base.db))
        # print(search)
        for dicionario in self.base.db:
            for value in dicionario:
                if nome == dicionario[value]:
                    return dicionario
                
                
    def selectAll(self)-> None:
        for dicionario in self.base.db:
            for value in dicionario:
                print(f'{value} -> {dicionario[value]}')
            print('-'*20)
                
                
    def updatedados(self,nome,new_name,new_idade,new_cpf)-> None:
        dados = self.selectForName(nome)
        dados["name"] = new_name
        dados["idade"] = new_idade
        dados["cpf"] = new_cpf
        print("dados alterados com sucesso!")
    
    def deleteForId(self,idx)-> None:
         for dicionario in self.base.db:
            for value in dicionario:
                if idx == dicionario[value]:
                    self.base.db.remove(dicionario)
                    print("cliente deletado com sucesso!") 
                    
                    
