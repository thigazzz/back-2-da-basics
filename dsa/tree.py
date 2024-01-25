"""

Árvores são estruturas formada por nós que se conectam entre si.
Diferente das Linked Lists, cada nó de uma árvore pode se conectar
com um ou mais nós

- Uma árvore é formada por um Nó 'ROOT', que é o ponto de partida para os demais nós.
- O antecessor de um Nó é denominado "Parent"
- O sucesso de um Nó é denominado "Child"
- O Nó ROOT não pode ter um Parent
- Um Nó não pode ser apontado mais de uma vez
- Cada filho pode ser representado por uma camada, level ou grau

# Tipos de Árvores
- Binary Trees: São arvores formada por dois filhos cada Nó (left e right)
"""
from typing import Optional, Any
class BinaryNode:
    def __init__(self, data: Any, left: Optional['BinaryNode'] = None, right: Optional['BinaryNode'] = None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.left} <- {self.data} -> {self.right}"

root = BinaryNode("ROOT")
root.left = BinaryNode("1 Left")
root.right = BinaryNode("1 Right")

class BinaryTree:
    def __init__(self) -> None:
        self.root: BinaryNode = None

    def add(self, value: int):
        node = BinaryNode(value)
        acc = self.root
        last_node: BinaryNode = None

        if acc == None:
            self.root = node
            return

        while acc:
            last_node = acc
            if value < acc.data:
                acc = acc.left
            else:
                acc = acc.right

        if value < last_node.data:
            last_node.left = node
        else:
            last_node.right = node

    def value_exists_in(self, value: int):
        root = self.root

        if root == None:
            return False
        
        while root:
            if root.data == value:
                return True

            if value < root.data:
                root = root.left
            else:
                root = root.right

        return False


binary_tree = BinaryTree()
binary_tree.add(5)
binary_tree.add(1)
binary_tree.add(3)
binary_tree.add(6)

binary_tree.add(10)
binary_tree.add(8)
print(binary_tree.root)

print(binary_tree.value_exists_in(10))