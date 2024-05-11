#!/usr/bin/python3
"""
Lockboxes
"""


def canUnlockAll(boxes):
    """
    method that determinates if all
    boxes can be opened
    """

    if not boxes:
        return False
    
    n = len(boxes)
    visitado = [False] * n
    visitado[0] = True
    cola = [0]

    while cola:
        caja_actual = cola.pop(0)
        for llave in boxes[caja_actual]:
            if 0 <= llave < n and not visitado[llave]:
                visitado[llave] = True
                cola.append(llave)

    return all(visitado)
