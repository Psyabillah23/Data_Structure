data = [20,10,45,25,12,24,2,5,7,24]
print(data)

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


