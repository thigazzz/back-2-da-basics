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

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

node_A = Node("A")
node_B = Node("B")
node_C = Node("C")

node_A.next = node_B
node_B.next = node_C
node_C.next = None

print(node_A.next) # Node B
print(node_B.next) # Node B
print(node_C.next) # Não tem proximo

print(node_A.next.next.data) # C

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add(self, data):
        node = Node(data)
        if self.head == None: # Setando o Head
            self.head = node
            return
        last_node = self.head
        while last_node.next: # Percorrendo todos os Nodes
            last_node = last_node.next # Setando o Node Atual como ultimo
        last_node.next = node # Setando o proximo Node

    def mid(self):
        if not self.head:
            return None

        slow_ptr = self.head
        fast_ptr = self.head
        
        # [1] -> [2] -> [3] -> [4] -> [5]
        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
            
        return slow_ptr.data

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

linked_list = LinkedList()
linked_list.add("1")
linked_list.add("2")
linked_list.add("3")
linked_list.add("4")
linked_list.add("5")
linked_list.add("6")
linked_list.add("7")

print(linked_list.mid())
assert linked_list.mid() == "4"
        