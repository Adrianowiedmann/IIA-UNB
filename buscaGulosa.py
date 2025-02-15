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
    
def busca_gulosa(grid, pos_inicial, pos_tesouro):
    explorado = []
    tam_colunas = len(grid)

    if pos_inicial == pos_tesouro:
        return [pos_tesouro]

    # Como heurística será utilizado a distância Manhattan
    def heuristica(pos_atual):
        return (abs(pos_atual[0] - pos_tesouro[0]) + abs(pos_atual[1] - pos_tesouro[1]))

    #borda = FilaPrioridade(0, ([pos_inicial], heuristica(pos_inicial, pos_tesouro)))
    borda = FilaPrioridade(heuristica(pos_inicial), [pos_inicial])

    while (1):
        if borda.is_empty():
            return []
        
        caminho = borda.remove()
        pos_atual = caminho[-1]

        if pos_atual not in explorado:
            if pos_atual == pos_tesouro:
                return caminho
            explorado.append(pos_atual)
            i, j = pos_atual
            if i+1 < tam_colunas:
                if grid[i+1][j] != '#':
                    borda.inserir(heuristica(pos_atual), caminho + [(i+1, j)])
            if i-1 >= 0:
                if grid[i-1][j] != '#':
                    borda.inserir(heuristica(pos_atual), caminho + [(i-1, j)])
            if j+1 < len(grid[i]):
                if grid[i][j+1] != '#':
                    borda.inserir(heuristica(pos_atual), caminho + [(i, j+1)])
            if j-1 >= 0:
                if grid[i][j-1] != '#':
                    borda.inserir(heuristica(pos_atual), caminho + [(i, j-1)])



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

caminho_gulosa = busca_gulosa(grid, pos_inicial, pos_tesouro)
print(caminho_gulosa)

grid = [
    ['I', '.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '.', '#', '#', '.', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.', '.'],
    ['#', '.', '#', '#', '#', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '.', '#', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '#', '.'],
    ['.', '.', '.', '#', '.', '.', '.', '.', '#', 'T'],
    ['.', '#', '#', '.', '#', '#', '.', '#', '#', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '#', '.'],
    ['.', '.', '#', '.', '#', '.', '#', '.', '.', '.'],
]
pos_inicial = (0, 0)
pos_tesouro = (6, 9)

caminho_gulosa = busca_gulosa(grid, pos_inicial, pos_tesouro)
print(caminho_gulosa)