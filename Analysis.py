import csv
import time


# Bubble Sort Algorithm
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# Selection Sort Algorithm
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        minimum = i

        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]


# Load dataset
def load_data(filename):
    numbers = []

    with open(filename, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            numbers.append(int(row[0]))

    return numbers


# Measure execution time
def analyze_algorithm(algorithm, data):
    start = time.time()

    algorithm(data)

    end = time.time()

    return end - start


data = load_data("dataset.csv")

bubble_time = analyze_algorithm(bubble_sort, data.copy())
selection_time = analyze_algorithm(selection_sort, data.copy())

print("Algorithm Analysis Result")
print("-------------------------")
print(f"Bubble Sort Time: {bubble_time:.6f} seconds")
print(f"Selection Sort Time: {selection_time:.6f} seconds")


if bubble_time < selection_time:
    print("Bubble Sort performed better on this dataset.")
else:
    print("Selection Sort performed better on this dataset.")
