"""Main module to run the program."""


def solve_sudoku(board: list[list[int]]) -> list[list[int]]:
    """Solves the board"""
    return resolve_sudoku(board)
    raise ValueError("Sudoku impossível de resolver")


def is_valid(board: list[list[int]]) -> bool:
    """Checks if the board is valid"""
    
    if len(board) != 9:
        return False
    
    return is_resolved(board)

def is_resolved(tabuleiro):
    #print(tabuleiro)
    for i in range(0, len(tabuleiro)):
        for j in range(0, len(tabuleiro)):
            
            linha = tabuleiro[i]
            coluna = [k[j] for k in tabuleiro]
            quadrantex = 0
            quadrantey = 0
            for q in range(0, len(tabuleiro)//3):
                if (q+1)*(len(tabuleiro)/3) > i:  
                    quadrantex = q
                    break
            for q in range(0, len(tabuleiro)//3):
                if (q+1)*(len(tabuleiro)/3) > j:  
                    quadrantey = q
                    break
            
            quadrante = []
            for a in range(0, 3): #obs adicione remover duplicados
                for b in range(0, 3):
                    quadrante.append(tabuleiro[a+quadrantex*(len(tabuleiro)//3)][b+quadrantey*(len(tabuleiro)//3)])
            
            numeros_possiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            
            for a in linha:
                if a in numeros_possiveis:
                    numeros_possiveis.remove(a)
            for a in coluna:
                if a in numeros_possiveis:
                    numeros_possiveis.remove(a)
            for a in quadrante:
                if a in numeros_possiveis:
                    numeros_possiveis.remove(a)
            #if numeros_possiveis[0] == 2:
            #print(numeros_possiveis)
            #print(i, j)
            dup = [x for i, x in enumerate(linha) if i != linha.index(x)]
            dup = list(filter(lambda a: a != 0, dup))
            #print(dup)
            if len(dup) > 0 and tabuleiro[i][j] != 0:
                return False
            dup = [x for i, x in enumerate(coluna) if i != coluna.index(x)]
            dup = list(filter(lambda a: a != 0, dup))
            if len(dup) > 0 and tabuleiro[i][j] != 0:
                return False
            dup = [x for i, x in enumerate(quadrante) if i != quadrante.index(x)]
            dup = list(filter(lambda a: a != 0, dup))
            if len(dup) > 0 and tabuleiro[i][j] != 0:
                return False    
            #if len(numeros_possiveis) == 0 and tabuleiro[i][j] == 0:
                #return False
            
    return True


def resolve_sudoku(tabuleiro):
    tabuleiro_modificado = tabuleiro
    modificador_escolha = 1 # 0=[x], 1=[x, y], 2=[x, y, z], etc
    cont = 0
    while cont < 100:
        
        #for i in tabuleiro_modificado:         
        #    print(i)
        #print("----------------")
    #while not is_resolved(tabuleiro_modificado):
        
        modificador_escolha = modificador_escolha - 1
        existeum = False # verifica se existe uma opção no formato [x] nesse loop, começa assumindo que não
        
        for i in range(0, len(tabuleiro)):
            for j in range(0, len(tabuleiro)):
                if tabuleiro_modificado[i][j] == 0:
                    retorno = scan_cell(tabuleiro_modificado, i, j, modificador_escolha, existeum)
                    opcoes = retorno[0]
                    modificador_escolha = retorno[1]
                    existeum = retorno[2]
                    if opcoes == '10':
                        pass
                    elif len(opcoes) == 1:
                        tabuleiro_modificado[i][j] = opcoes[0]
        if existeum:
            modificador_escolha = modificador_escolha + 1 # permanece 0 no proximo loop
        else:
            modificador_escolha = modificador_escolha + 2 # vira um no próximo loop
        cont = cont + 1
    return tabuleiro_modificado
    #tab = resolve_sudoku(tabuleiro_modificado)
    #return tab


def scan_cell(tabuleiro_modificado, i, j, modificador_escolha, existeum):
    linha = tabuleiro_modificado[i]
    coluna = [k[j] for k in tabuleiro_modificado]
    quadrantex = 0
    quadrantey = 0
    for q in range(0, len(tabuleiro_modificado)//3):
        if (q+1)*(len(tabuleiro_modificado)/3) > i:  
            quadrantex = q
            break
    for q in range(0, len(tabuleiro_modificado)//3):
        if (q+1)*(len(tabuleiro_modificado)/3) > j:  
            quadrantey = q
            break
    
    quadrante = []
    for a in range(0, 3): #obs adicione remover duplicados
        for b in range(0, 3):
            quadrante.append(tabuleiro_modificado[a+quadrantex*(len(tabuleiro_modificado)//3)][b+quadrantey*(len(tabuleiro_modificado)//3)])
        
    #print(f"quadrante-{i}-{j}: {quadrante}")
    
    
    numeros_possiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for a in linha:
        if a in numeros_possiveis:
            numeros_possiveis.remove(a)
    for a in coluna:
        if a in numeros_possiveis:
            numeros_possiveis.remove(a)
    for a in quadrante:
        if a in numeros_possiveis:
            numeros_possiveis.remove(a)
    
    #print(f"{i}-{j}: {numeros_possiveis}")
    #if len(numeros_possiveis) == 0:
        #return [0]
    if len(numeros_possiveis) == 1:
        existeum = True
        return [numeros_possiveis, modificador_escolha, existeum]
    elif len(numeros_possiveis) == 2 and modificador_escolha == 1:
        modificador_escolha = modificador_escolha - 1
        return [[numeros_possiveis[0]], modificador_escolha, existeum]
    else:
        return ['10', modificador_escolha, existeum]
    #if len(numeros_possiveis) > 1:
        #return numeros_possiveis


#def remove_repetidos(lista):
#    l = []
#    for i in lista:
#        if i not in l:
#            l.append(i)
#    l.sort()
#    return l


def check_if_is_complete(tabuleiro):  #checa se o tabuleiro está completo
    pass


def check_if_is_possible(
        tabuleiro):  #checa se ainda tem algum número possivel de se jogar
    pass

#'''
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
    tab2 = [
            [0, 4, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 4, 0, 0, 6, 0, 3],
            [0, 0, 1, 0, 7, 9, 0, 2, 0],
            [7, 0, 0, 0, 0, 8, 0, 0, 2],
            [9, 0, 0, 0, 3, 0, 0, 0, 1],
            [6, 0, 0, 9, 0, 0, 0, 0, 7],
            [0, 7, 0, 3, 1, 0, 8, 0, 0],
            [1, 0, 9, 0, 0, 4, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 1, 0],
        ]
    tab3 = [[1 for x in range(9)] for y in range(9)]
    is_valid(tab)
    #resolve_sudoku(tab3)
#'''
