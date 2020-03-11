"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    return first == second

    


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:

    return type(first) == type(second)
    


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:

    return first is second



def multiple_ints(first_value: int, second_value: int) -> int:
    if(isinstance(first_value, bool)  & isinstance(second_value, bool) ):
        raise TypeError
   
    elif (isinstance(first_value, int)  & isinstance(second_value, int) ):
        return first_value * second_value
    else:
        raise TypeError
    
    


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    try:
        return int (first_value) * int(second_value)
    except (ValueError, TypeError):
        raise ValueError
        
    


def is_word_in_text(word: str, text: str) -> bool:

    return word in text


def some_loop_exercise() -> list:
    
    return [i for i in range(0,13) if ((i!=6) & (i!=7))]
    


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
  
    return [data[i] for i in range(len(data)) if (data[i]>0)]


def alphabet() -> dict:

    return {i : chr(i + 96) for i in range (1,27)} 
    """
    Create dict which keys are alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """


def simple_sort(data: List[int]) -> List[list]:
    for i in range(len(data)):
        lowest_value_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[lowest_value_index]:
                lowest_value_index = j
        data[i], data[lowest_value_index] = data[lowest_value_index], data[i]
    return data

    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    """
    