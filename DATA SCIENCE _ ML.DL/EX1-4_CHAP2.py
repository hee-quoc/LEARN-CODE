
# Ex1: Write a NumPy program to reverse an array (first element becomes last).
# Input: [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]
import numpy as np
data1 = [12,13,14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
def exercise1(data):
    print("Before: ")
    print(data)
    reversed = data[::-1]
    print("After:")
    print(reversed)

# Ex2: Write a NumPy program to test whether each element of a 1-D array is also present in a second array
# Input Array1: [ 0 10 20 40 60]
#       Array2: [10, 30, 40]
import numpy as np
data2_1 =  [ 0,10,20,40,60]
data2_2 = [10, 40]
def exercise2(data1,data2):
    print(f"Data 1 :{data1}")
    print(f"Data 2 :{data2}")
    presented_check = np.in1d(data2,data1)
    checked = np.all(presented_check)

    print(f'Is each element of a 1-D array is also present in a second array: {checked}')

# Ex3: Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array
# Input Array [1,6,4,8,9,-4,-2,11]
data3 = [1,6,4,8,9,-4,-2,11]
def exercise3(data):
    print(data)
    print(f'Index of maximum value: {np.argmax(data)}\nIndex of minimum value: {np.argmin(data)}')

# Ex4
import numpy as np
import string
from collections import Counter
import os

characters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

def delete_special_characters(words):
    table = str.maketrans('', '', string.punctuation)
    corrected = []
    for word in words:
        if len(word) == 1 and word in characters:
            continue

        corrected_word = word.translate(table).lower()
        corrected.append(corrected_word)
        
    return corrected


def exercise4():
    word_counter = Counter()
    

    if not os.path.exists('D:\IU documents\YEAR3\LEARN CODE\DATA SCIENCE _ ML.DL\HY-DATASCIENCE-ML_DL\story.txt'):
        print("Error: The file 'story.txt' does not exist.")
        return
    
    try:
        with open('D:\IU documents\YEAR3\LEARN CODE\DATA SCIENCE _ ML.DL\HY-DATASCIENCE-ML_DL\story.txt', 'r') as f:
            for line in f:
                words = line.strip().split()
                corrected_words = delete_special_characters(words)
                word_counter.update(corrected_words)
        
        most_common = word_counter.most_common(100)
        print("Top 100 words occur most frequently.")
        for word, count in most_common:
            print(f'{word}: {count}')
    
    except Exception as e:
        print(f"An error occurred: {e}")

exercise4()
