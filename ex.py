#pip install sympy graphviz
#pip install sympy
#pip install Pillow
import sympy as sp
from sympy.logic.boolalg import *
from graphviz import Digraph
from PIL import Image

def transformar_expressao(expressao):
    expr_sympy = sp.sympify(expressao, evaluate=False)
    
    # Função para eliminar implicações e bicondicionais
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
        # Aplicar a transformação recursivamente para subexpressões
        return expr.func(*map(eliminar_condicionais, expr.args))
    
    # Eliminar implicações e bicondicionais
    expr_transformada = eliminar_condicionais(expr_sympy)
    
    return expr_transformada

def simplificar_expressao(expr_transformada):
    expr_sympy = sp.sympify(expr_transformada, evaluate=False)
    expr_simplificada = sp.simplify_logic(expr_sympy)
    
    return expr_simplificada

def gerar_diagrama(expr, nome_arquivo):
    def adicionar_nodos(expr, grafo, pai=None):
        if expr.is_Atom:
            grafo.node(str(expr), str(expr))
            if pai:
                grafo.edge(str(pai), str(expr))
        elif isinstance(expr, Not):
            nodo = f'Not_{str(expr.args[0])}'
            grafo.node(nodo, 'NOT')
            if pai:
                grafo.edge(str(pai), nodo)
            adicionar_nodos(expr.args[0], grafo, nodo)
        else:
            nodo = f'{str(expr.func)}_{str(expr)}'
            grafo.node(nodo, str(expr.func))
            if pai:
                grafo.edge(str(pai), nodo)
            for sub_expr in expr.args:
                adicionar_nodos(sub_expr, grafo, nodo)
    
    grafo = Digraph()
    adicionar_nodos(expr, grafo)
    grafo.render(nome_arquivo, format='png', cleanup=True)

def exibir_imagem(nome_arquivo):
    img = Image.open(f"{nome_arquivo}.png")
    img.show()

def main():
    expressao_entrada = input("Digite uma expressão lógica: ")
    expressao_entrada = expressao_entrada.replace("<->", "==").replace("->", ">>").replace("V", "|").replace("or", "|").replace("and", "&").replace("∧", "&")
    
    try:
        # Transformação da expressão
        expressao_transformada = transformar_expressao(expressao_entrada)
        # Simplificação da expressão
        expressao_simplificada = simplificar_expressao(expressao_transformada)
        
        # Gerar diagramas
        gerar_diagrama(expressao_transformada, "circuito_original")
        gerar_diagrama(expressao_simplificada, "circuito_simplificado")
        
        expressao_saida = str(expressao_simplificada).replace(">>", "->").replace("==", "<->").replace("|", "V").replace("&", "∧")
        print("Expressão simplificada:", expressao_saida)
        print("Circuitos gerados: 'circuito_original.png' e 'circuito_simplificado.png'")
        
        # Exibir imagens
        exibir_imagem("circuito_original")
        exibir_imagem("circuito_simplificado")
    except Exception as e:
        print("Erro ao processar a expressão:", e)

if __name__ == "__main__":
    main()