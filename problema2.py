from collections import defaultdict, deque

def bfs_find_leaves(tree, n, root):
    """ Encuentra todas las hojas del árbol usando BFS. """
    degree = [0] * n  # Grado de cada nodo (número de conexiones)
    leaves = []  # Lista de hojas
    
    for u in tree:
        degree[u] = len(tree[u])
    
    # Las hojas son los nodos con grado 1 (excepto la raíz si es hoja)
    for i in range(n):
        if degree[i] == 1 and i != root:
            leaves.append(i)
    
    return leaves

def count_groups(tree, n, root, k):
    """ Cuenta cuántos grupos pueden formarse con cabañas consecutivas en el árbol. """
    # Si no hay suficientes cabañas o k es 0, no hay grupos posibles
    if n == 0 or k == 0:
        return 0
    
    leaves = bfs_find_leaves(tree, n, root)
    groups = 0
    visited = set()
    queue = deque(leaves)

    while queue:
        current = queue.popleft()
        
        if current in visited:
            continue

        # Intentamos formar un grupo de k cabañas consecutivas desde la hoja
        path = []
        node = current
        
        while node not in visited and len(path) < k:
            path.append(node)
            visited.add(node)
            
            # Buscar el padre en el árbol
            for neighbor in tree[node]:
                if neighbor not in visited:
                    node = neighbor
                    break
        
        if len(path) == k:
            groups += 1  # Se formó un grupo válido
    
    return groups

def main():
    import sys
    input = sys.stdin.read
    lines = input().strip().split("\n")

    # Leer número de cabañas y cabañas por grupo
    n, k = map(int, lines[0].split())

    # Si no hay cabañas, la respuesta es 0
    if n == 0:
        print(0)
        return

    # Construcción del árbol (grafo no dirigido)
    tree = defaultdict(list)
    for line in lines[1:]:
        u, v = map(int, line.split())
        tree[u].append(v)
        tree[v].append(u)

    # Llamamos a la función que cuenta los grupos posibles
    resultado = count_groups(tree, n, 0, k)
    print(resultado)

if __name__ == '__main__':
    main()
