"""
Array é um tipo de estrutura de dado que armazena
uma quantidade limitada de itens do mesmo tipo sequencialmente
na memória, podendo accesar esses itens pelo seu index.

Representação na Memória:
    array[3] = ['A', 'B', 'C']
    [] [] [2] []
    [4] [3] [] []
    [None] [A] [B] [C] (armazenado sequencialmente)

Sua principal vantagem é sua simplicade e praticidade.

Um array é capaz de armazenar diversos itens sem a
necessidade de criar diversas variáveis.

Principais operações de um array:

- Acessar um elemento O(1)
- Percorrer o array O(n)
- Adicionar um item O(n)
- Deletar um item O(n)
- Procurar um item O(n)
- Atualizar um item O(n)

O array é incapaz de passar do seu limite, pois
como o espaço na memória já foi definido, é possivel
que o proximo slot na memória já esteja ocupado.
"""
import array as a
"""
Módulo para trabalhar como arrays
"""

# a.array(tipo dos elementos do array, lista com os elementos)                    
new_array = a.array('i', [1,2,3,4,5])

def index(arr, index):
    try:
        return arr[index]
    except:
        return "No index"
def transversal(arr):
    for i in range(len(arr)):
        print(arr[i])

def add(arr, item):
    arr.append(item)


assert index(new_array, 2) == 3
assert index(new_array, 5) == "No index"
transversal(new_array)
add(new_array, 6)
assert index(new_array, 5) == 6
