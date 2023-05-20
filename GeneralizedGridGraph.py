# Konstantinos Malamas 2748
import random

def create_grid_graph(n):
    row_edge = n
    grid_graph = []

    for i in range(n + 1):
        print("i is: ", i)
        grid_graph.append([])
        for d in range(row_edge):  # left up corner vertices dont have value, so we give them -1 score
            grid_graph[i].append(-1)

        if i == 0:  # the source has value 0 and the rest of the first row has value (0,d-1) + 1
            grid_graph[i].append(0)
            for d in range(n, 2 * n):
                grid_graph[i].append(grid_graph[i][d] + 1)
        else:  # computing the minimum path of the vertex
            for d in range(row_edge, row_edge + n + 1):
                if d == row_edge:
                    grid_graph[i].append(i)
                    continue
                print("d is ", d)
                random_number = random.random()
                print(random_number)
                if random_number < 0.5:
                    substitution_cost = 0
                else:
                    substitution_cost = 1
                print(substitution_cost)

                vertex_cost = min(grid_graph[i - 1][d] + substitution_cost,
                                  grid_graph[i][d - 1] + 1,
                                  grid_graph[i - 1][d + 1] + 1)

                grid_graph[i].append(vertex_cost)

            for d in range(n - row_edge):  # also vertices with no value (-1) to the right down corner of the grip graph
                grid_graph[i].append(-1)

        row_edge -= 1
    for i in range(0, n + 1):  # printing the grid graph
        print(grid_graph[i])
    return grid_graph[n][n]  # the sink
