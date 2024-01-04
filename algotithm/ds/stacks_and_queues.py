"""
Stacks e Queues são coleções de dados que tem
o comportamento de entrada e saída, sendo lineares
ou seja, tem uma ordem a seguir.
A diferença entre as duas é o comportamento e o
fluxo de entrada e sáida dos elementos.

STACKS
reprensentada por uma pilha ou empilhamento.
Seu fluxo é de último a entrar, primeiro a sair
(last in, first out) ou (LIFO)

QUEUES
reprensentada por uma fila de espera.
Seu fluxo é de primeiro a entrar, primeiro a sai
(first in, first out) ou (FIFO)


"""

#  Stack Implentation

"""
As stacks podem funcionar em arrays ou linked lists.
Seu comportamento é de adicionar e remover.
Essa implementação pode ser feita a partir de 
um ponteiro que aponta para o topo (ou ultimo elemento)

            top
          pointer

[1] - [2] - [3]

push(elemento): top = top + 1; lista[top] = elemento
pop(): top = top - 1

Na deleção, o valor do ultimo elemento não precisa ser modificado
ou deletado, basta apenas mudar a referencia do ponteiro.

"""

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1

    def push(self, element):
        self.stack.append(element)

    def pop():
        self.stack.pop()

    def get_top(self):
        return self.stack[self.top]



stack = Stack()

stack.push("hello")

assert stack.get_top() == "hello"
