"""Main module to run the program."""


def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    return board
    raise ValueError("Sudoku impossível de resolver")


def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    
    if len(board) != 9:
        return False

    return True

def is_resolved(tabuleiro):
    print(tabuleiro)
    for i in range(0, len(tabuleiro)):
        for j in range(0, len(tabuleiro)):
            if tabuleiro[i][j] == 0:
                 return False
    return True


def resolve_sudoku(tabuleiro):
    tabuleiro_modificado = tabuleiro
    
    cont = 0
    while cont < 10:
        for i in tabuleiro_modificado:         
            print(i)
        print("----------------")
    #while not is_resolved(tabuleiro_modificado):
        for i in range(0, len(tabuleiro)):
            for j in range(0, len(tabuleiro)):
                if tabuleiro_modificado[i][j] == 0:
                    ops = scan_line(tabuleiro_modificado, i, j)
                    if ops != 10:
                        tabuleiro_modificado[i][j] = ops[0]
        cont = cont + 1
    return tabuleiro_modificado
    #tab = resolve_sudoku(tabuleiro_modificado)
    #return tab


def scan_line(tabuleiro_modificado, i, j):
    linha = tabuleiro_modificado[i]
    coluna = [k[j] for k in tabuleiro_modificado]
    numeros_possiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for a in linha:
        if a in numeros_possiveis:
            numeros_possiveis.remove(a)
    for a in coluna:
        if a in numeros_possiveis:
            numeros_possiveis.remove(a)
    print(f"{i}-{j}: {numeros_possiveis}")
    #if len(numeros_possiveis) == 0:
        #return [0]
    if len(numeros_possiveis) == 1:
        return numeros_possiveis
    elif len(numeros_possiveis) == 2:
        return [numeros_possiveis[0]]
    else:
        return 10
    #if len(numeros_possiveis) > 1:
        #return numeros_possiveis


def scan_column(coluna):
    pass


def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


def check_if_is_complete(tabuleiro):  #checa se o tabuleiro está completo
    pass


def check_if_is_possible(
        tabuleiro):  #checa se ainda tem algum número possivel de se jogar
    pass


if __name__ == "__main__":
    tab = [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
           [6, 0, 0, 1, 9, 5, 0, 0, 0],
           [0, 9, 8, 0, 0, 0, 0, 6, 0], 
           [8, 0, 0, 0, 6, 0, 0, 0, 3],
           [4, 0, 0, 8, 0, 3, 0, 0, 1], 
           [7, 0, 0, 0, 2, 0, 0, 0, 6],
           [0, 6, 0, 0, 0, 0, 2, 8, 0], 
           [0, 0, 0, 4, 1, 9, 0, 0, 5],
           [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    resolve_sudoku(tab)
        

