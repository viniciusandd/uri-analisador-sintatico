from flask import jsonify
from flask_restful import Resource
from .parsers import retornar_parser
from ..commons import TabelaDeParsing, Pilha, Entrada, Automato


class AnalisadorSintatico(Resource):
    def get(self):
        parser = retornar_parser()
        args = parser.parse_args()
        sentenca = args['sentenca']        
        
        pilha = Pilha()
        entrada = Entrada(sentenca)
        tabela_parsing = TabelaDeParsing()
        automato = Automato(pilha, entrada)
        
        while True:
            acao = tabela_parsing.acao(pilha.topo(), entrada.inicio())
            automato.adicionar_linha(acao)
            if acao == "DESEMPILHAR_E_LER":
                pilha.desempilhar()
                entrada.ler()
            elif acao and acao != "ACEITA":
                pilha.modificar_topo(acao)
            else:
                break
                        
        return jsonify(automato.tabela)