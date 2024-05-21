import random
import time

def create_random_array(array_length):
    
    random_array = []   
    
    # Використовуємо цикл для додавання випадкових чисел до масиву
    for _ in range(array_length):
        random_number = random.randint(1, array_length * 10)
        random_array.append(random_number)
    
    return random_array

def sort(array):
    start_time = time.time()
    comparisons = 0
    swaps = 0

    # Проходимо через кожен елемент масиву
    for i in range(len(array)):
        # Проходимо через масив, починаючи з i+1 елемента
        for j in range(i + 1, len(array)):
            comparisons += 1  # Кожний раз, коли порівнюємо елементи, збільшуємо лічильник порівнянь
            if array[i] > array[j]:
                # Якщо поточний елемент більший за наступний, міняємо їх місцями
                array[i], array[j] = array[j], array[i]
                swaps += 1  # Збільшуємо лічильник обмінів

    end_time = time.time()
    time_taken = end_time - start_time
    return comparisons, swaps, time_taken

# Створюємо масиви
array_sizes = [100, 1000, 10000]
for size in array_sizes:
    array = create_random_array(size)
    comparisons, swaps, time_taken = sort(array)
    print(f"Array size: {size}")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps: {swaps}")
    print(f"Time taken: {time_taken:.5f} seconds\n")
    
    

    
