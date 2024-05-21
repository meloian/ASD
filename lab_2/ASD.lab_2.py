import numpy as np
import time

def generate_array(length):
    return np.random.randint(-1000, 1000, length)

def selection_sort(arr):
    # Implements the selection sort algorithm.
    comparisons = 0
    swaps = 0
    for i in range(len(arr)):
        # assume the first unsorted element is the minimum
        min_idx = i
        # search the rest of the array for a smaller element
        for j in range(i+1, len(arr)):
            comparisons += 1  
            if arr[min_idx] > arr[j]:
                min_idx = j  
        # swap the found minimum element with the first unsorted position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if min_idx != i:
            swaps += 1  
    return comparisons, swaps

def sedgewick_steps(size):
    # generates Sedgewick's gap sequence for shell sort
    steps = []
    i = 0
    while True:
        # calculate gap using Sedgewick's formula
        if i % 2 == 0:
            step = 9 * (2**i - 2**(i // 2)) + 1
        else:
            step = 8 * (2**i - 2**((i + 1) // 2)) + 1
        if step > size:
            break  
        steps.append(step)  
        i += 1
    return steps[::-1]  

def shell_sort_sedgewick(arr):
    # implements the Shell sort algorithm using Sedgewick's gap sequence
    comparisons = 0
    swaps = 0
    steps = sedgewick_steps(len(arr))
    for step in steps:
        # perform insertion sort for each gap size
        for i in range(step, len(arr)):
            temp = arr[i]
            j = i
            while j >= step and arr[j - step] > temp:
                comparisons += 1
                arr[j] = arr[j - step]  
                swaps += 1  
                j -= step
            # place temp at its correct position
            arr[j] = temp
    return comparisons, swaps 

def measure_sorting(sort_function, array_lengths, repetitions=10):
    # measures and aggregates the sorting performance over multiple repetitions for accuracy
    results = {}
    for length in array_lengths:
        total_comparisons, total_swaps, total_time = 0, 0, 0.0
        # use multiple repetitions for arrays up to length 1000 for more reliable metrics
        if length <= 1000:  
            for _ in range(repetitions):
                arr = generate_array(length)
                start_time = time.time()
                comparisons, swaps = sort_function(arr.copy())
                end_time = time.time()
                # agregate the performance metrics
                total_comparisons += comparisons
                total_swaps += swaps
                total_time += end_time - start_time
            # calculate average performance metrics
            avg_comparisons = total_comparisons / repetitions
            avg_swaps = total_swaps / repetitions
            avg_time = total_time / repetitions
        else:  # for arrays with length 10000, perform a single measurement
            arr = generate_array(length)
            start_time = time.time()
            avg_comparisons, avg_swaps = sort_function(arr.copy())
            avg_time = time.time() - start_time
        # store the results for each array size
        results[length] = {
            'comparisons': avg_comparisons,
            'swaps': avg_swaps,
            'time': avg_time
        }
    return results

# measure and print the efficiency for all specified array sizes
array_lengths = [100, 1000, 10000]
selection_results = measure_sorting(selection_sort, array_lengths)
shell_sedgewick_results = measure_sorting(shell_sort_sedgewick, array_lengths)

print("Selection Sort Results:", selection_results)
print("Shell Sort (Sedgewick) Results:", shell_sedgewick_results)
