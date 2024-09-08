#!/usr/bin/env python3
def return_evens(num_list):
    return [n for n in num_list if n % 2 == 0]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(return_evens(numbers))  



def make_exclamation(sentence_list):

   return [sentence + "!" for sentence in sentence_list]
string = (["Hello", "I'm doing great", "Python is fun"])
print (make_exclamation(string))