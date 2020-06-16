class TabelaDeParsing:
    def __init__(self):
        """
        Os valores da tabela são estáticos.
        """
        self.conteudo = {}
        self.conteudo["S","a"] = "aA"
        self.conteudo["S","b"] = None
        self.conteudo["S","c"] = None
        self.conteudo["S","$"] = None
        self.conteudo["A","a"] = "aBc"
        self.conteudo["A","b"] = None
        self.conteudo["A","c"] = None
        self.conteudo["A","$"] = "&"        
        self.conteudo["B","a"] = None
        self.conteudo["B","b"] = None
        self.conteudo["B","c"] = "cCa"
        self.conteudo["B","$"] = None        
        self.conteudo["C","a"] = None
        self.conteudo["C","b"] = "bB"
        self.conteudo["C","c"] = "c"
        self.conteudo["C","$"] = None
    
    def buscar(self, nao_terminal = None, terminal = None):
        return self.conteudo[nao_terminal, terminal] if not nao_terminal and not terminal else self.conteudo

class Pilha:
    def __init__(self):
        self.conteudo = ["$", "S"]

    def buscar(self):
        return self.conteudo

class Entrada:
    def __init__(self, sentenca):
        self.conteudo = list(sentenca + "$")
    
    def buscar(self):
        return self.conteudo    

