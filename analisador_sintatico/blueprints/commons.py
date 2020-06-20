class Auxiliar:
    def conteudo_to_string(self):
        return ''.join(self.conteudo)      

class TabelaDeParsing:
    def __init__(self):
        """
        Os valores da tabela são estáticos.
        """
        self.conteudo = {}
        self.conteudo["S","a"] = "aAb"
        self.conteudo["S","b"] = None
        self.conteudo["S","c"] = None
        self.conteudo["S","d"] = None
        self.conteudo["S","$"] = None     

        self.conteudo["A","a"] = "aBc"
        self.conteudo["A","b"] = None
        self.conteudo["A","c"] = None
        self.conteudo["A","d"] = "dC"
        self.conteudo["A","$"] = None

        self.conteudo["B","a"] = None
        self.conteudo["B","b"] = "bC"
        self.conteudo["B","c"] = "&"
        self.conteudo["B","d"] = None
        self.conteudo["B","$"] = None     

        self.conteudo["C","a"] = None
        self.conteudo["C","b"] = None
        self.conteudo["C","c"] = "c"
        self.conteudo["C","d"] = "dA"
        self.conteudo["C","$"] = None                     
                
    def acao(self, char1, char2):
        if char1 == char2:
            if char1 == "$":
                return "ACEITA"
            return "DESEMPILHAR_E_LER"
        return self.conteudo[char1, char2]

class Pilha(Auxiliar):
    def __init__(self):
        self.conteudo = ["$", "S"]

    def topo(self):
        return self.conteudo[len(self.conteudo) - 1]
    
    def modificar_topo(self, acao):
        self.conteudo.pop()
        if acao == "&":
            return
        lista_de_chars = list(acao)
        lista_de_chars.reverse()        
        for c in lista_de_chars:
            self.conteudo.append(c)
        
    def desempilhar(self):
        self.conteudo.pop()    

class Entrada(Auxiliar):
    def __init__(self, sentenca):
        self.conteudo = list(sentenca + "$")
    
    def inicio(self):
        return self.conteudo[0]
    
    def ler(self):
        self.conteudo.pop(0)

class Automato:
    def __init__(self, pilha: Pilha, entrada: Entrada):
        self.tabela = []
        self.pilha = pilha
        self.entrada = entrada

    def mensagens(self, acao):
        if acao == "DESEMPILHAR_E_LER":
            return "Desempilhar e ler %s" % self.pilha.topo()
        elif acao == "ACEITA":
            return f"Aceita em {len(self.tabela) + 1} iterações"
        elif not acao:
            return f"Erro em {len(self.tabela) + 1} iterações. O símbolo não pode ser produzido."
        else:
            return "%s -> %s" % (self.pilha.topo(), acao)

    def adicionar_linha(self, acao):
        linha = {
            "pilha": self.pilha.conteudo_to_string(),
            "entrada": self.entrada.conteudo_to_string(),
            "acao": self.mensagens(acao)
        }
        self.tabela.append(linha)