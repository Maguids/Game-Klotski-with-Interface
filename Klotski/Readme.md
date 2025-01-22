 
---------PuzzlePacked IQ games---------
Na nossa versão do jogo "PuzzlePacked IQ games", o objetivo é mover o maior bloco e posicioná-lo no lugar certo. Para fazer isso, é necessário mover um conjunto de blocos menores, permitindo que o bloco maior se mova.
O tabuleiro do jogo é composto por uma grelha retangular de células, e os blocos são colocados nessa grelha. Cada bloco ocupa uma ou mais células, e os blocos podem mover-se em qualquer uma das quatro direções cardeais (para cima, para baixo, para a esquerda ou para a direita), desde que não haja obstáculos no caminho.

---Funcionalidades---
Interface gráfica simples;
Possibilidade de escolher diferentes tabuleiros com níveis de dificuldade diferentes;
Oportunidade de utilizar de voltar (sempre) para o 'Menu', de dar restart no nível e de terminar o jogo ('Quit');
Opção de escolher o search algorithm desejado;
Função de dica ('hint'), que varia de acordo com o search algorithm utilizado, que mostra a próxima jogada possível.
 
---Algoritmos de Busca---
Os seguintes algoritmos de busca foram implementados para resolver os diferentes níveis de dificuldade:
    Breadth-First Search (BFS) - Utiliza uma fila para explorar estados e encontrar a solução.
 A função retorna o caminho para a solução ou None se não houver solução dentro da profundidade máxima definida.
    Greedy Best-First Search - Utiliza a heurística da distância de Manhattan para ordenar os estados na fila de prioridade. O objetivo é encontrar a solução com a menor quantidade de movimentos possíveis.
 A função retorna uma lista de movimentos que levam à solução, ou "None" caso não seja possível encontrar uma solução dentro da profundidade máxima.
    A* Algorithm (A Star) - Utiliza uma fila de prioridade, um conjunto de estados visitados, um caminho e uma contagem de profundidade para explorar estados e encontrar a solução.
 O algoritmo usa a distância de Manhattan como heurística e a soma da distância heurística e do custo do caminho percorrido como custo total. 
 A função retorna o caminho para a solução ou None se não houver solução dentro da profundidade máxima definida.

---Requisitos---
Python;
Bibliotecas Pygame, Sys, Copy.

---Como usar---
Instale a biblioteca Pygame, se ainda não tiver sido instalada.
Aceda ao terminal e verifique que está dentro do diretório 'jogo' para ter acesso.
Execute o comando 'python3 start.py' e escolha se deseja jogar o jogo no Pygame ou no terminal.
Selecione a dificuldade desejada e escolha um nivel.
Use o rato para mover as peças do tabuleiro, se em pygame, ou indique a peça e o movimento, se em terminal.
Os espaços vazios, ou seja, locais para onde se podem movimentar as peças, estão representados por espaços brancos em Pygame e por zeros no Terminal.
Se precisar de ajuda, clique no botão 'Hint' para ver a próxima jogada possível.
Tente mover as peças até libertar o bloco vermelho. No caso do Pygame o bloco será 'liberto' pela fenda na barreira do jogo (desenhada a preto) e no Terminal representada por espaços vazios (' ').
Explore as outras possibilidades do 'Menu', em Pygame, tal como a seleção do search algorithm que deseja e da porfundidade a que o algoritmo tem acesso, ou então no Terminal quando selecioana a 'hint'.


 -----------------------------------------------------------------------------------------------------------------------
| Trabalho desenvolvido para a cadeira de Elementos de Inteligencia Artificial e Ciencia de Dados, realizado por:       |
|                                                                                                                       |
|  - Magda Costa, up202207036                                                                                           |
|  - Sofia Machado, up202207203                                                                                         |
|                                                                                                                       |
|                                                                                                                       |
| Esperamos que gostem!                                                                                                 |
|                                                                                                                       |
 -----------------------------------------------------------------------------------------------------------------------

 