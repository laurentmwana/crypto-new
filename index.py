# Algorithme pour la génération des clés de Feistel


def gapLeft(a: list) -> list[int]:
    return a[2:] + a[0:2] 


def gapRight(a: list) -> list[int]:
    
    return []


def andLogicGate(a: list, b: list, size: int = 4) -> list[int]:
    output = []
    for index in range(0, size - 1):
        output.append(1) if a[index] == 1 and b[index] == 1 else output.append(0)
    return output

def xorLogicGate(a: list, b: list, size: int = 4) -> list[int]:
    output = []
    for index in range(0, size - 1):
        output.append(1) if a[index] != b[index] else output.append(0)
    return output

def generateKey(k: str) -> list:
    """ Permet de génerer une clé """
    # Appliquer la fonction de permutation H = 65274130
    hIndexer = (3, 1, 2, 0, 4, 7, 5, 6)
    kIndexer = list(map(int, k))
    kPrime = []
    for h in hIndexer:
        kPrime.append(kIndexer[h])
    # Diviser K en deux blocs de 4 bits : K = k
    kPrime1, kPrime2 = kPrime[0:4], kPrime[4:8]
    # k1 = k′1 ⊕ k′2 et k2 = k′2 ∧ k′1
    k1, k2 = xorLogicGate(kPrime1, kPrime2), andLogicGate(kPrime1, kPrime2)
    
    
    
    return [k1, k2]
    

print(gapLeft([1, 0, 1, 1]))
