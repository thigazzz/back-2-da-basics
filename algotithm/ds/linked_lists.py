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

    def __repr__(self) -> str:
        return f"[val: {self.data}, next: {self.next}]" 

node_A = Node("A")
node_B = Node("B")
node_C = Node("C")

node_A.next = node_B
node_B.next = node_C
node_C.next = None

# print(node_A.next) # Node B
# print(node_B.next) # Node B
# print(node_C.next) # Não tem proximo

# print(node_A.next.next.data) # C

class SingleLinkedList:
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

    def remove_last(self):
        if not self.head:
            return None
        
        head = self.head
        
        # [1] -> [2] -> [3] -> [4] -> [5]
        while head != None:
            if head.next.next == None:
                head.next = None
            head = head.next
            
    def remove_item(self, item):
        accr = self.head

        while accr.next != None:
            # [1] -> [2] -> [3] -> [4]

            if accr.next.data == item:
                accr.next = accr.next.next
                break

            accr = accr.next

    def mid(self):
        if not self.head:
            return None

        accr = self.head
        after = self.head
        
        # [1] -> [2] -> [3] -> [4] -> [5]
        while after.next:
            accr = accr.next
            after = after.next.next
            
        return accr.data
    

    def count(self):
        c = 0
        head = self.head
        while head != None:
            c += 1
            head = head.next
        return c

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

linked_list = SingleLinkedList()
linked_list.add("1")
linked_list.add("2")
linked_list.add("3")
linked_list.add("4")
linked_list.add("5")


assert linked_list.count() == 5

assert linked_list.mid() == "3"

linked_list.remove_last()
assert linked_list.count() == 4

linked_list.remove_item('1')
linked_list.print_list()
