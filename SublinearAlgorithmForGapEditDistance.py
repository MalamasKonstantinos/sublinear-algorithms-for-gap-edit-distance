# Konstantinos Malamas 2748
import math
import random

from RandomStringGenerator import generate_random_strings


def calculate_gap_edit_distance(a_string, b_string, n, t):
    l = 2 * t + 1
    c_A = []  # cost array
    for w in range(l):
        c_A.append(0)
    D = []  # Boolean array for active vertices
    active_sum = 0
    d = 0  # supporting variable

    D_next = [False for y in range(l)]  # Boolean array for next
    D_next[t] = True
    D_j = []

    mode = "sampling mode"
    rate = math.log10(n) / t

    # pattern
    p_string = []
    i_pat = 0
    g = 0
    for i in range(n-t):
        random_rate = random.random()

        if mode == "contiguous mode":  # CONTIGUOUS MODE

            D.append(D_next)
            D_next = [False for y in range(2 * t + 1)]  # Clearing D_next

            for d in range(0, l):
                if D[i][d]:
                    if c_A[d] > t - abs(d - t):
                        continue

                    elif check_if_potent(D, d, c_A, i, a_string, b_string, t):
                        D_next[d] = True
                        if a_string[i] != b_string[i + d - t]:
                            if d < 2 * t:
                                D[i][d + 1] = True
                            if d > 0:
                                D_next[d - 1] = True
                            c_A[d] += 1

            max_d = get_max_diagonal(D[i], 2 * t + 1) # change d next to d i
            min_d = get_min_diagonal(D[i], 2 * t + 1)

            if not search_for_missmatch(i, t, max_d, min_d, a_string, b_string, D):
                g = get_gcd_of_difference(D[i], 2 * t + 1, t)
                i_pat = i - 2 * (max_d - min_d) + 1
                t_max_d = max_d
                t_min_d = min_d
                p_string.clear()
                p_string = get_pattern_string(i_pat, i_pat + g - 1, a_string)  # m changed index because list starts from 0
                mode = "sampling mode"


        elif (mode == "sampling mode" and random_rate < rate) or i == t:  # SAMPLING MODE
            D.append(D_next)  # check if it starts with sampling mode, to be sure
            D_next = [False for y in range(l)]  # Clearing D_next
            active_sum = get_active_sum(D[i], l)


            if active_sum == 1:  # SHIFT CHECK
                d = D[i].index(True)

                if a_string[i] == b_string[i + d - t]:
                    D_next[d] = True
                else:
                    c_A[d] += 1

                    D_next[d] = True
                    if d < l - 1:
                        D_next[d + 1] = True
                    if d > 0 :
                        D_next[d - 1] = True
                    mode = "contiguous mode"


            elif active_sum > 1:  # PERIODICITY CHECK
                max_d = get_max_diagonal(D[i], 2 * t + 1)
                min_d = get_min_diagonal(D[i], 2 * t + 1)

                if a_string[i] == b_string[i + max_d - t] and a_string[i] == p_string[(i - i_pat + 1) % g]:  # string moddified for %
                    D_next = D[i]
                else:
                    j = detect_row_j(i, t, i_pat, a_string, b_string, p_string, t_max_d, t_min_d, g)
                    if j is None:
                        D_next = [False for y in range(l)]  # Boolean array for next
                        D_next[t] = True
                    else :
                        D_j = [False for y in range(2 * t + 1)]

                        for x in range(j, j + max_d - min_d):
                            for d_x in range(0, 2 * t + 1):
                                if D[i][d_x] and a_string[x] != b_string[x + d_x - t] and not D_j[d_x]:
                                    c_A[d_x] += 1
                                    D_next[d_x] = True
                                    D_next[d_x + 1] = True
                                    D_next[d_x - 1] = True
                                    D_j[d_x] = True
                        for d_x in range(0, 2 * t + 1):
                            if D[i][d_x] != D_j[d_x]:
                                D_next[d_x] = True

                                for y in range(i_pat, i):
                                    if random.random() < rate and a_string[y - 1] != b_string[y + d_x - t - 1]:
                                        c_A[d_x] += 1
                                        D_next[d_x + 1] = True
                                        D_next[d_x - 1] = True
                                        break
                                break
                        mode = "contiguous mode"
                        flagerino = "OMG YESSS"

        elif (mode == "sampling mode" and random_rate >= rate) or i < t:
            D.append([False for y in range(l)])

        if c_A[t] >= t + 1:  # Stopping Condition
            print("Far")
            result = "far"
            return result


    D.append(D_next)
    print(c_A)
    print("close")
    result = "close"
    return result


def get_active_sum(S, l):
    active_sum = 0
    for d in range(l):
        if S[d]:
            active_sum += 1

    return active_sum


def get_max_diagonal(S, l):
    max_d = 0
    for d in range(l - 1, -1, -1):
        if S[d]:
            max_d = d
            break

    return max_d


def get_min_diagonal(S, l):
    min_d = l

    for d in range(0, l):
        if S[d]:
            min_d = d
            break

    return min_d


def get_gcd_of_difference(S, l, t):
    temp_gcd = 0
    first = True
    for d1 in range(l):
        for d2 in range(l):
            if first and S[d1] and S[d2] and d1 > d2:
                temp_gcd = (d1 - t) - (d2 - t)
                first = False
            elif not first and S[d1] and S[d2] and d1 > d2:
                temp_gcd = math.gcd(temp_gcd, (d1 - t) - (d2 - t))
    return temp_gcd


def get_pattern_string(left_edge, right_edge, original_string):
    return original_string[left_edge:right_edge + 1]


def detect_row_j(i, t, i_pat, a_string, b_string, p_string, max_d, min_d, g):  # UNDER WORK
    sum_j = 0
    S_possible = []
    for j_temp in range(i_pat, i + 1):  # i+1 to include i
        if a_string[j_temp - 1] == b_string[j_temp + max_d - t - 1] and a_string[j_temp - 1] == p_string[(j_temp - i_pat) % g]:
            sum_j += 1
            if sum_j >= 2 * (max_d - min_d):
                S_possible.append(j_temp)
        else:
            sum_j = 0
    for j in S_possible:
        if a_string[j] != p_string[(j + 1 - i_pat) % g]:
            return j
        elif b_string[j + max_d - t] != p_string[(j + 1 - i_pat) % g]:
            return j


def check_if_potent(S, d, c, i, a_string, b_string, t): #fix bug
    if d == 2 * t:
        if (not (c[d - 1] == c[d] - 1)) or (S[i][d - 1] and a_string[i] != b_string[i + (d - t) - 1]):
            return True
        else:
            return False
    elif d == 0 or i + (d - t) - 1 <= 0:
        if (not (c[d + 1] == c[d] - 1)) or (S[i - 1][d + 1] and a_string[i - 1] != b_string[(i - 1) + (d - t) + 1]):
            return True
        else:
            return False
    elif ((not (c[d - 1] == c[d] - 1)) or (S[i][d - 1] and a_string[i] != b_string[i + (d - t) - 1])) and (
            (not (c[d + 1] == c[d] - 1)) or (S[i - 1][d + 1] and a_string[i - 1] != b_string[(i - 1) + (d - t) + 1])):
        return True
    else:
        return False


def search_for_missmatch(i, t, max_d, min_d, a_string, b_string, S):
    class Found(Exception):
        pass
    try:
        for temp_i in range(i - 2 * (max_d - min_d) + 1, i + 1):
            if temp_i < 0:
                continue
            for temp_d in range(0, 2 * t + 1):
                if temp_i - 1 + temp_d - t < 0:
                    continue
                elif S[temp_i][temp_d] and a_string[temp_i - 1] != b_string[temp_i - 1 + temp_d - t]:
                    raise Found
    except Found:
        return True
    return False







