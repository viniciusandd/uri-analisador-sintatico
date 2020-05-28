from flask_restful import reqparse

def retornar_parser():
    parser = reqparse.RequestParser()
    parser.add_argument('sentenca', type=str, required=True)    
    return parser
