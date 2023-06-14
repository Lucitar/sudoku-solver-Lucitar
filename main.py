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


def resolve_sudoku(tabuleiro):
    tabuleiro_modificado = tabuleiro
    for i in range(0, len(tabuleiro)):
        for j in range(0, len(tabuleiro)):
            if tabuleiro_modificado[i][j] == 0:
                scan_line(tabuleiro_modificado[i])
            
def scan_line(linha):
    for i in linha:
        pass

def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

def scan_column(tabuleiro, coluna):
    pass

def check_if_is_complete(tabuleiro): #checa se o tabuleiro está completo
    pass

def check_if_is_possible(tabuleiro): #checa se ainda tem algum número possivel de se jogar
    pass

if __name__ == "__main__":
    print('a')

