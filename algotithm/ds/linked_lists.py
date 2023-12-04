"""
Linked Lists são um conjunto de items linkados uns com outros,
Cada item é um Node que armazena um dado e um ponteiro para o proximo Item,
Esse tipo de estrutura de dados é usado em situações em que a lista de dados é grande,
além de ser flexivel ao aumentar ou diminuir sua dimensão de modo a não consumir muita memoria.


Exemplo:

Node Head       Node 1        Node 2        Node 3 (Ultimo nó)
[5, Node1] -> [2, Node2] -> [8, Node3] -> [1, Null]

[Dado, Ponteiro para o proximo Nó]

Existem tipos de Linked Lists:
- Singles Linked List: Navegação apenas para a direita
- Doubly Linked List: Navegação para direita e esquerda
- Circular Linked List: Navegação circular, sendo que o ultimo aponta para o primeiro Nó

Exemplos da vida-real:
- Navegação Web: Com as Linked Lists é possivel avançar e voltar páginas Web sem perder seus endereços.
Além dessa possibilidade, há economia na memoria pois os items são estão sendo processados a cada novo clique
"""
