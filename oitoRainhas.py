def check_rainhas(rainhas, nova_rainha):
    x1, y1 = nova_rainha[0], nova_rainha[1]
    for i in range(len(rainhas)):
        rainha = rainhas[i]
        x, y = rainha[0], rainha[1]

        if x != x1 and y != y1:
            if abs((y1 - y)) == abs((x1 - x)):
                return False
        else:
            return False    
        
    return True


print(check_rainhas([(2, 2)], (4, 4)))
print(check_rainhas([(1, 3), (2, 1)], (3, 6)))