import heapq

"""
Será utilizado o heap como estrutura de dados subjacente para 
a implementação da fila de prioridade. 
"""

# Classe que implementa a fila de prioridade 
class FilaPrioridade:
    def __init__(self, custo, item):
        self.lista = []  # Armazena os elementos da fila de prioridade
        heapq.heappush(self.lista, (custo, item))

    # Adiciona um elemento na fila com sua prioridade
    def inserir(self, custo, item):
        heapq.heappush(self.lista, (custo, item))

    # Verifica se a fila de prioridade está vazia
    def is_empty(self):
        return len(self.lista) == 0

    # Remove o elemento de maior prioridade e retorna
    def remove(self):
        return heapq.heappop(self.lista)[1]

def busca_custo_uniforme(grid, pos_inicial, pos_tesouro):
    borda = FilaPrioridade(0, ([pos_inicial], 0))
    explorado = []

    # Sabemos o tamanho das colunas
    # mas não sabemos o tamanho das listas (não foi especificado no trabalho)
    tam_colunas = len(grid)

    while (1):
        # Retorna lista vazia caso não tenha mais elemento na borda
        if borda.is_empty():
            return []
        
        # Armazena como nó somente o último elemento do caminho,
        # pois é ele que fornecerá os próximos elementos da borda
        caminho, custo = borda.remove()
        no = caminho[-1]

        if pos_inicial == pos_tesouro:
            return [pos_tesouro]
        
        if no not in explorado:
            if pos_tesouro == no:
                return caminho
            
            explorado.append(no)
            novo_custo = 0
            i, j = no
            if i+1 < tam_colunas:
                if grid[i+1][j] != '#':
                    novo_custo = custo + (5 if grid[i+1][j] == 'L' else 1)
                    borda.inserir(novo_custo, (caminho + [(i+1, j)], novo_custo))
            if i-1 >= 0:
                if grid[i-1][j] != '#':
                    novo_custo = custo + (5 if grid[i-1][j] == 'L' else 1)
                    borda.inserir(novo_custo, (caminho + [(i-1, j)], novo_custo))
            if j+1 < len(grid[i]):
                if grid[i][j+1] != '#':
                    novo_custo = custo + (5 if grid[i][j+1] == 'L' else 1)
                    borda.inserir(novo_custo, (caminho + [(i, j+1)], novo_custo))
            if j-1 >= 0:
                if grid[i][j-1] != '#':
                    novo_custo = custo + (5 if grid[i][j-1] == 'L' else 1)
                    borda.inserir(novo_custo, (caminho + [(i, j-1)], novo_custo))

grid = [
    ['I', '#', '.', '#', 'L', 'L', 'T'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '#', 'L', '#', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.'],
]

pos_inicial = (0, 0)
pos_tesouro = (0, 6)

caminho_bcu = busca_custo_uniforme(grid, pos_inicial, pos_tesouro)

print(caminho_bcu)