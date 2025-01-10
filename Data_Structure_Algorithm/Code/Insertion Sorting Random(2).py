import random #import library

data = random.sample(range(1, 1000), 50) #mengambil 50 sample data random range angka 1-200
print("Angka Sebelum Diurutkan : ", data)

def insertionSort(arr): #mendefinisikan sebuah fungsi
    for i in range(1, len(arr)): #melakukan iterasi sampai akhir list
        key = arr[i] 
        j = i - 1
        while j >= 0 and key < arr[j]: #melakukan iterasi mundur
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertionSort(data) #memanggil fungsi
print("Setelah diurutkan dengan Insertion Sort: ", data)
