import sympy as sp
from sympy.logic.boolalg import *
from graphviz import Digraph
from PIL import Image

def transformar_expressao(expressao):
    expr_sympy = sp.sympify(expressao, evaluate=False)
    
    def eliminar_condicionais(expr):
        if expr.is_Atom:
            return expr
        if isinstance(expr, Implies):
            a, b = expr.args
            return Or(Not(eliminar_condicionais(a)), eliminar_condicionais(b))
        if isinstance(expr, sp.Eq):
            a, b = expr.args
            return And(Or(Not(eliminar_condicionais(a)), eliminar_condicionais(b)),
                       Or(Not(eliminar_condicionais(b)), eliminar_condicionais(a)))
        return expr.func(*map(eliminar_condicionais, expr.args))
    
    expr_transformada = eliminar_condicionais(expr_sympy)
    
    return expr_transformada

def simplificar_expressao(expr_transformada):
    expr_simplificada = sp.simplify_logic(expr_transformada)
    return expr_simplificada

def gerar_diagrama(expr, nome_arquivo):
    def adicionar_nodos(expr, grafo, pai=None, id_counter=None):
        if id_counter is None:
            id_counter = {}

        if expr.is_Atom:
            if expr not in id_counter:
                id_counter[expr] = 0
            nodo = f"{expr}_{id_counter[expr]}"
            grafo.node(nodo, str(expr))
            if pai:
                grafo.edge(pai, nodo)
            id_counter[expr] += 1
        elif isinstance(expr, Not):
            nodo = f'Not_{str(expr.args[0])}_{id_counter.get(expr.args[0], 0)}'
            grafo.node(nodo, 'NOT')
            if pai:
                grafo.edge(pai, nodo)
            adicionar_nodos(expr.args[0], grafo, nodo, id_counter)
        else:
            nodo = f'{str(expr.func)}_{str(expr)}'
            grafo.node(nodo, str(expr.func))
            if pai:
                grafo.edge(pai, nodo)
            for sub_expr in expr.args:
                adicionar_nodos(sub_expr, grafo, nodo, id_counter)
    
    grafo = Digraph(format='png')
    grafo.attr(rankdir='LR')
    adicionar_nodos(expr, grafo)
    grafo.render(nome_arquivo, format='png', cleanup=True)

def exibir_imagem(nome_arquivo):
    img = Image.open(f"{nome_arquivo}.png")
    img.show()

def main():
    expressao_entrada = input("Digite uma expressão lógica: ")
    expressao_entrada = expressao_entrada.replace("<->", "==").replace("->", ">>").replace("V", "|").replace("or", "|").replace("and", "&").replace("∧", "&")
    
    try:
        expressao_transformada = transformar_expressao(expressao_entrada)
        expressao_simplificada = simplificar_expressao(expressao_transformada)
        
        gerar_diagrama(expressao_transformada, "circuito_original")
        gerar_diagrama(expressao_simplificada, "circuito_simplificado")
        
        expressao_saida = str(expressao_simplificada).replace(">>", "->").replace("==", "<->").replace("|", "V").replace("&", "∧")
        print("Expressão simplificada:", expressao_saida)
        print("Circuitos gerados: 'circuito_original.png' e 'circuito_simplificado.png'")
        
        exibir_imagem("circuito_original")
        exibir_imagem("circuito_simplificado")
    except Exception as e:
        print("Erro ao processar a expressão:", e)

if __name__ == "__main__":
    main()
