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
        """

        metodo para adicionar um elemento
        no topo da stack, ou pilha.
        
        stack:
        [0]

        stack.push(4)
        [4] (sempre no topo)
        [0]

        """
        self.stack.append(element)
        self.top += 1

    def pop(self):
        """
        Método para remover o elemento
        no topo da stack, ou pilha

        stack:
        [2]
        [7]

        stack.pop()
        [7]

        """
        self.stack.pop()
        self.top -= 1

    def is_empty(self):
        """
        Retorna se a lista está ou não 
        vazia

        Se o top for -1, quer dizer que a stack
        está vazia

        """
        return self.top == -1

    def peek(self):
        """
        Pega o elemento do topo da Stack, ou pilha

        """
        return self.stack[self.top] 

    def get_top(self):
        return self.stack[self.top]



stack = Stack()

assert stack.is_empty() == True, "Era para ser True"

stack.push("hello")

assert stack.get_top() == "hello"
assert stack.top == 0

stack.push("...")
stack.push("...")
stack.push("Ultimo valor")

assert stack.peek() == "Ultimo valor", "Era para ser Ultimo valor"
assert stack.top == 3

stack.pop()


assert stack.top == 2

assert stack.is_empty() == False, "Era para ser False"

print("TESTE CORRETOS")
