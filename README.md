# Simplificação Circuito
Crie um programa que simplifique circuito lógicos.<br>
<b>Regras:</b><br>
1. Dada uma expressão (sentença) lógica, apresente graficamente a sentença em forma de circuito lógico;<br>
2. Simplifique o circuito e apresente os passos da simplificação.<br>
3. Apresente o resultado da simplificação na forma de um circuito.<br><br>

<h1>COMO USAR</h1>
<h5>#1. INSTALE AS SEGUINTES BIBLIOTECAS NO TERMINAL</h5>
    #pip install sympy<br>
    #pip install graphviz<br>
    #pip install Pillow<br>

<h5>#2. Baixe e instale Graphviz no seguinte link:</h5>
    'https://gitlab.com/api/v4/projects/4207231/packages/generic/graphviz-releases/11.0.0/windows_10_cmake_Release_graphviz-install-11.0.0-win64.exe'<br>
<h5>#3. Encontrar o diretório de instalação do Graphviz (Normalmente fica no endereço 'C:\Program Files\Graphviz\bin')</h5>
<h5>#4. Adicionar ao PATH</h5>
    # Abra o "Painel de Controle".<br>
    # Vá até "Sistema e Segurança" e clique em "Sistema".<br>
    # Clique em "Configurações avançadas do sistema" no lado esquerdo.<br>
    # Na aba "Avançado", clique no botão "Variáveis de Ambiente".<br>
    # Na seção "Variáveis do sistema", encontre a variável Path e selecione-a. Clique em "Editar".<br>
    # Adicione o caminho para o diretório onde o dot.exe está instalado. Por exemplo, C:\Program Files\Graphviz\bin.<br>
    # Clique em "OK" para fechar todas as janelas.<br>
<h5>#5. Reinicie o terminal e verifique se foi certamente instalado digitando no Terminal (CMD)</h5>
    'dot -version'<br><br>

<h1>Exemplos:</h1>
<b>Entrada:</b><br>
((A ∧ B) V ((C V A) ∧ ~B))<br>
<b>Saída 1:</b><br>

![image](https://github.com/VicRuk/simplificacao-circuito/assets/99752207/3b45cb1b-0af3-4647-8265-39e24461546f)<br>
<b>Saída 2:</b><br>
(A v (C ∧ ~B))<br>
(Resultado do circuito SIMPLIFICADO da fórmula de entrada):<br>
![image](https://github.com/VicRuk/simplificacao-circuito/assets/99752207/3d9c8548-505e-41aa-a1c4-96e2388504c5)<br>
