# Python Sorting Algorithms

This project demonstrates the implementation of three sorting techniques in Python:
1. **Bubble Sort** - A simple comparison-based sorting algorithm.
2. **Merge Sort** - A divide-and-conquer sorting algorithm.
3. **Sorting Words in a List** - Sorting words lexicographically in a list.

## Table of Contents
- [Overview](#overview)
- [Bubble Sort](#bubble-sort)
- [Merge Sort](#merge-sort)
- [Sorting Words in a List](#sorting-words-in-a-list)

---

## Overview

Sorting is a fundamental task in computer science, with various algorithms available to arrange elements in a specific order (ascending or descending). This project implements two common sorting algorithms: **Bubble Sort** and **Merge Sort**, along with a utility for **sorting words in a list**.

## Bubble Sort

### Algorithm Explanation:
Bubble Sort is a simple algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

### Time Complexity:
- **Best Case**: O(n)
- **Average Case**: O(n^2)
- **Worst Case**: O(n^2)

### Python Code:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example Usage
arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted Array:", bubble_sort(arr))
```

## Merge Sort

### Algorithm Explanation:
Merge Sort is a recursive divide-and-conquer algorithm. It divides the array into two halves, recursively sorts both halves, and then merges the two sorted halves.



### Time Complexity:
- **Best Case**: O(n log n)
- **Average Case**: O(n log n)
- **Worst Case**: O(n log n)

### Python Code:

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Example Usage
arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted Array:", merge_sort(arr))
```

## Sorting Words in a List

### Algorithm Explanation:
Sorting words in a list can be done lexicographically (alphabetically). Python’s built-in ```sort()``` function or ```sorted()``` method can be used to sort strings in a list.


### Python Code:

```python
def sort_words(words):
    return sorted(words)

# Example Usage
words_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
sorted_words = sort_words(words_list)
print("Sorted Words:", sorted_words)
```

#### Python’s Built-in Sorting:
Python provides efficient built-in sorting methods like sort() and sorted() that utilize Timsort, which is a hybrid of Merge Sort and Insertion Sort with O(n log n) time complexity.