from ShortestPathInASampledGridGraphAlgorithm import calculate_edit_distance_sampled
from ShortestPathInAGridGraphAlgorithm import calculate_edit_distance
from SublinearAlgorithmForGapEditDistance import calculate_gap_edit_distance
from RandomStringGenerator import generate_random_strings
from WagnerFisherEditDistance import calculate_edit_distance_wf
import time

for x in range(1000):
    print("Type length of strings n:")
    n = int(input())
    print("Set Hamming distance between the two strings")
    dd = int(input())
    print("Type the parameter t:")
    t = int(input())
    a_string, b_string = generate_random_strings(n, dd)


    start = time.time()
    result = calculate_gap_edit_distance(a_string, b_string, n, t)
    a_string, b_string = generate_random_strings(n, dd)
    #result2 = calculate_edit_distance_wf(a_string, b_string)
    end = time.time()

    start2 = time.time()
    #result2 = calculate_gap_edit_distance(a_string, b_string, n, t)
    end2 = time.time()

    print("result is: ", result)
    #print("result is: ", result2)
    print("execution time: ", end - start, " seconds")

    #print("result sublinear is: ", result2)
    #print("execution time: ", end2 - start2, " seconds")

#calculate_gap_edit_distance(a_string, b_string, n, t)
