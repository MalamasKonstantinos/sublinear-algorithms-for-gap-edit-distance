# Konstantinos Malamas 2748
import math
import random

from RandomStringGenerator import generate_random_strings


def calculate_edit_distance_sampled(a_string, b_string, n, t):
    row_edge = t
    grid_graph = []
    j = 0
    previous_i = 0
    rate = math.log10(n) / t  # possibility
    random_number = 0   # so that i0 is included

    for i in range(n + 1):
        if random_number < rate:  # Sampling the rows
            grid_graph.append([])
            for d in range(row_edge):  # left up corner vertices dont have value, so we give them -1 score
                grid_graph[j].append(-1)

            if j == 0:  # the source has value 0 and the rest of the first row has value (0,d-1) + 1
                grid_graph[j].append(0)
                for d in range(t, 2 * t):
                    grid_graph[j].append(grid_graph[j][d] + 1)

            else:  # computing the minimum path of the vertex
                for d in range(row_edge, 2 * t + 1):
                    if d == row_edge:
                        grid_graph[j].append(j)  #
                        continue

                    if (n - previous_i <= t) and (previous_i + d - t >= n)  :
                        grid_graph[j].append(-1)
                        continue

                    if previous_i + d - t > n:
                        grid_graph[j].append(-1)
                        continue

                    if a_string[previous_i] == b_string[previous_i + d - t]:
                        substitution_cost = 0
                    else:
                        substitution_cost = 1

                    if d == 2 * t:
                        vertex_cost = min(grid_graph[j - 1][d] + substitution_cost,
                                          grid_graph[j][d - 1] + 1)
                    else:
                        vertex_cost = min(grid_graph[j - 1][d] + substitution_cost,
                                          grid_graph[j][d - 1] + 1,
                                          grid_graph[j - 1][d + 1] + 1)

                    grid_graph[j].append(vertex_cost)

            j += 1
            if row_edge > 0:
                row_edge -= 1
            previous_i = i
        random_number = random.random()

    temp_t = -t
    n0_value = grid_graph[-1][0] + abs(temp_t)

    for i in range(1, 2*t + 1):
        temp_t += 1
        if n0_value > grid_graph[-1][i] + abs(temp_t) and grid_graph[-1][i] != -1:
            n0_value = grid_graph[-1][i] + abs(temp_t)

    print("sink value is :", n0_value)
    if n0_value < t:
        print("Close")
    else:
        print("Far")

    return grid_graph[j - 1][t]  # the sink
