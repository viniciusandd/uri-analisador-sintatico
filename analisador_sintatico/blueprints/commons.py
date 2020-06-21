import random

class Auxiliar:
    def conteudo_to_string(self):
        return ''.join(self.conteudo)      

class Sentenca(Auxiliar):
    def __init__(self):
        self.conteudo = ['a', 'A', 'b']
    
    def localizar_nao_terminal(self):
        for producao in self.conteudo:
            if len(producao) == 1:
                if producao.isupper():
                    return producao
            else:
                for char in producao:
                    if char.isupper():
                        return producao
        return None

    def gerar(self):
        tabela_parsing = TabelaDeParsing()
        while True:
            nao_terminal = self.localizar_nao_terminal()
            if not nao_terminal:
                break
            producoes = tabela_parsing.buscar_producoes(nao_terminal)
            producao = producoes[0] if len(producoes) == 1 else producoes[random.randint(0, len(producoes)-1)]
            index = self.conteudo.index(nao_terminal)
            if producao != '&':
                self.conteudo[index] = producao
                string_conteudo = self.conteudo_to_string()
                self.conteudo = list(string_conteudo)      
            else:
                self.conteudo.remove(nao_terminal)
        return self.conteudo_to_string()

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
        try:
            producao = self.conteudo[char1, char2]
            return producao
        except:
            return None        

    def buscar_producoes(self, terminal):
        producoes = []
        for producao in self.conteudo:
            if producao[0] == terminal:
                if self.conteudo[producao]:
                    producoes.append(self.conteudo[producao])
        return producoes

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
            return f"Erro em {len(self.tabela) + 1} iterações."
        else:
            return "%s -> %s" % (self.pilha.topo(), acao)

    def adicionar_linha(self, acao):
        linha = {
            "pilha": self.pilha.conteudo_to_string(),
            "entrada": self.entrada.conteudo_to_string(),
            "acao": self.mensagens(acao)
        }
        self.tabela.append(linha)