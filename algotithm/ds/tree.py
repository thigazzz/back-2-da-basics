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
from typing import Optional
class BinaryNode:
    def __init__(self, data: str, left: Optional['BinaryNode'] = None, right: Optional['BinaryNode'] = None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"{self.left} <- {self.data} -> {self.right}"

root = BinaryNode("ROOT")
root.left = BinaryNode("1 Left")
root.right = BinaryNode("1 Right")
