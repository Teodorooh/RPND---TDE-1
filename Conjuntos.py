#Eduardo Teodoro Moreira de Souza
''' Enunciado!
Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a
linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de
operações que serão realizadas entre dois conjuntos de dados.
O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)
contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas
seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da
operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e
terceira linhas conterão os elementos dos conjuntos separados por virgulas.A seguir está um exemplo
das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
4
U
3, 5, 67, 7
1, 2, 3, 4
I
1, 2, 3, 4, 5
4, 5
D
1, A, C, 34
A, C, D, 23
C
3, 4, 5, 5, A, B, R
1, B, C, D, 1
Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e
{𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
a informação e a formatação mostrada a seguir:
União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}
Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e
minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e
pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no
ambiente repl.it quanto no ambiente Github.
'''

#Abrir e ler o arquivo de texto
with open ("entrada1.txt", "r", encoding="utf-8") as file:
    entradaX = file.readlines()

#Por se transformar em vetor, o "1" representa a linha "2" do arquivo.txt
linha = 1
#Verificar a quantidade de operações
linhaZero = int (entradaX[0].strip())

#Estrutura que vai repetir de acordo com a quantidade de operações
for item in range (linhaZero):
    op = entradaX[linha].strip() #Linha que indica a operação
    conjunto1 = set(entradaX[linha+1].strip().split()) #Linha subsequente à operação (Conjunto 1)
    conjunto2 = set(entradaX[linha+2].strip().split()) #Linha subsequente ao conjunto 1 (Conjunto 2)
    
    if "U" in op:
        print(f"União: Conjunto 1 {conjunto1}, Conunto 2 {conjunto2}. Resultado: {conjunto1.union(conjunto2)}")
    elif "I" in op: 
        print(f"Intersecção: Conjunto 1 {conjunto1}, Conunto 2 {conjunto2}. Resultado: {conjunto1.intersection(conjunto2)}")
    elif "D" in op:
        print(f"Diferença: Conjunto 1 {conjunto1}, Conunto 2 {conjunto2}. Resultado: {conjunto1.difference(conjunto2)}")
    elif "C" in op:
        produtoCartesiano = {(x, y) for x in conjunto1 for y in conjunto2} #Calcular o Produto Cartesiano
        print(f"Produto Cartesiano: Conjunto 1 {conjunto1}, Conunto 2 {conjunto2}. Resultado: {produtoCartesiano}") 
    linha += 3 #Passa para as próximas operações
