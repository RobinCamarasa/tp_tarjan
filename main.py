import sys


def new_graph(n, file_name):
    graph = []
    for i in range(n):
        graph.append([])
    file_in = open(file_name, 'r')
    c = 0
    for line in file_in:
        (i,j) = line.split('\t', 1)
        (j,k) = j.split('\n',1)
        graph[int(i)].append(int(j))
        c += 1
    print('Le graph contenant ' +
          str(n) +
          'sommet(s) et '
          + str(c) +
          'arretes a ete cree')
    return graph


def new_visited_table(n):
    visited = []
    for i in range(n):
        visited.append(0)
    return visited


def tarjan(n, graph):
    result = False
    loading = 1
    for i in range(n):
        if (100 * i) / n > loading:
            print('Sommets visites : ' + str(loading) + ' pourcents')
            loading = (100 * i) / n
        result = result or tarjan_rec(graph, i, new_visited_table(n), n)
    return result


def tarjan_rec(graph, i, visisted_table, n):
    visisted_table[i] += 1
    if visisted_table[i] > 1:
        print(str(i))
        return True
    cycle = False
    for j in graph[i]:
        cycle = cycle or tarjan_rec(graph, j, visisted_table, n)
    return cycle


if __name__ == "__main__":
    n = int(sys.argv[2])
    if tarjan(n+1, new_graph(n+1, sys.argv[1])):
        print ('Ce graph contient un cycle')
    else:
        print ('Ce graph ne contient pas de cycle')
