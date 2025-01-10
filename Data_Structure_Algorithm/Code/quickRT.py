import random
import time

def quick_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# List untuk menyimpan waktu proses sorting
sorting_times = []

# List untuk menyimpan jumlah angka yang diurutkan
number_of_elements = []

# Loop untuk menguji algoritma sorting dengan berbagai ukuran array
for n in range(10, 110, 10):#melakukan iterasi untuk nilai n mulai dari 10 hingga 100 dengan selang 10
    arr = random.sample(range(1, 500), n) #angka acak yang diambil dari rentang 1 hingga 500
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
