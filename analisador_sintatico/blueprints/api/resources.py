from flask import jsonify
from flask_restful import Resource
from .parsers import retornar_parser
from ..commons import TabelaDeParsing, Pilha, Entrada, Automato, Sentenca


class AnalisadorSintatico(Resource):
    def get(self):
        parser = retornar_parser()
        args = parser.parse_args()
        sentenca = args['sentenca']        
        
        if len(sentenca) == 0:
            resposta = jsonify({"erro": "A sentença não pode ser vazia."})
            resposta.status_code = 400
            return resposta

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
    
class GerarSentenca(Resource):
    def get(self):
        sentenca = Sentenca()
        sentenca_gerada = sentenca.gerar()
        return jsonify({"sentenca": sentenca_gerada})