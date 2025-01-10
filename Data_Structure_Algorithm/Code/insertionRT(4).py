import random
import time
import matplotlib.pyplot as plt

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr):
    size = len(arr)
    stack = [(0, size - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            if pivot_index - low < high - pivot_index:
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))
            else:
                stack.append((pivot_index + 1, high))
                stack.append((low, pivot_index - 1))

# List untuk menyimpan waktu proses sorting
sorting_times = []

# List untuk menyimpan jumlah angka yang diurutkan
number_of_elements = []

# Loop untuk menguji algoritma sorting dengan berbagai ukuran array
for n in range(10, 110, 10):
    arr = random.sample(range(1, 500), n)
    print("Angka Sebelum Diurutkan: ")
    print(arr)
    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    print("Angka Setelah Diurutkan: ")
    print(arr)
    sorting_time = end_time - start_time
    sorting_times.append(sorting_time)
    number_of_elements.append(n)

    # Membuat plot menggunakan matplotlib
plt.plot(number_of_elements, sorting_times, marker='o', linestyle='-')
plt.title('Running Time vs Jumlah Angka yang Diurutkan (Quick Sort)')
plt.xlabel('Jumlah Angka yang Diurutkan')
plt.ylabel('Waktu Proses Sorting (detik)')
plt.grid(True)
plt.show()
