def kosaraju(G):
    # Step 1: Compute the reverse G
    G_reverso = G.reverse()

    # Step 2: First DFS to compute finishing times
    visitados = set()
    tempo_finalizacao = []

    def dfs1(vi):
        visitados.add(vi)
        for adjacente in G.adjacentes(vi):
            if adjacente not in visitados:
                dfs1(adjacente)
        tempo_finalizacao.append(vi)

    for vi in G.nodes():
        if vi not in visitados:
            dfs1(vi)

    # Step 3: Second DFS to find strongly connected components
    visitados.clear()
    componentes_fconexos = []

    def dfs2(vi, componente):
        visitados.add(vi)
        componente.add(vi)
        for adjacente in G_reverso.adjacentes(vi):
            if adjacente not in visitados:
                dfs2(adjacente, componente)

    while tempo_finalizacao:
        vi = tempo_finalizacao.pop()
        if vi not in visitados:
            componente = set()
            dfs2(vi, componente)
            componentes_fconexos.append(componente)

    return componentes_fconexos