# Konstantinos Malamas 2748
# String to String Correction Problem by Robert A. Wagner and Michael J. Fischer


def calculate_edit_distance_wf(a_string, b_string):
    D = [[0]]
    alength = len(a_string)
    blength = len(b_string)

    for a in range(1, alength + 1):
        D.append([a])

    for b in range(1, blength + 1):
        D[0].append(b)

    for b in range(1, blength + 1):
        for a in range(1, alength + 1):
            if a_string[a - 1] == b_string[b - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1

            x = D[a - 1][b] + 1                         # deletion
            y = D[a][b - 1] + 1                         # insertion
            z = D[a - 1][b - 1] + substitution_cost     # substitution

            D[a].append(min(x, y, z))

    #print_array(D, a_string, b_string)
    return D[alength][blength]


def print_array(D, a_string, b_string):
    a_string.insert(0, " ")
    b_string.insert(0, " ")
    x = 0
    print(" ", end = "")
    for y in b_string:
        print("  " + y, end="")
    print("")

    for i in D:
        print(a_string[x], i)
        x += 1


#print("Enter First String:")
#original_a_string = input()
#a_string = list(original_a_string)
#print("Enter Second String:")
#original_b_string = input()
#b_string = list(original_b_string)
#result = calculate_edit_distance_wf(a_string, b_string)
#print("Edit Distance between '" + original_a_string+"' and '" + original_b_string + "' is ", result)
