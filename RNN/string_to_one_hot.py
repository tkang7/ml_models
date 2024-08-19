# a utils function to convert charactes into one hot encoded vectors   

import string
import numpy as np

def string_to_one_hot(inputs: np.ndarray) -> np.ndarray:
    char_to_index = {c: i for i, c in enumerate(string.ascii_uppercase)}
    one_hot_inputs = []

    for row in inputs:
        one_hot_list = []
        for char in row:
            if char.upper() in char_to_index:
                one_hot_vector = np.zeros((len(string.ascii_uppercase), 1))
                one_hot_vector[char_to_index[char.upper()]] = 1
                one_hot_list.append(one_hot_vector)
        one_hot_inputs.append(one_hot_list)

    return np.array(one_hot_inputs)