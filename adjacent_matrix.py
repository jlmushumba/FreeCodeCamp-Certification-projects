def adjacency_list_to_matrix(data):
    adjacency_matrix = []
    rows = len(data)
    columns = rows

    for i in range(rows):
        the_list = []
        for j in range(columns) :
            if j not in data[i]:
                the_list.append(0)
            elif j in data[i]:
                the_list.append(1)
        adjacency_matrix.append(the_list)

    for k in adjacency_matrix:
        print(k)

    return adjacency_matrix

adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})