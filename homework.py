"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    if (first == second):
        result = True
    else:
        result = False
    print (result)
    return result

    pass


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    type_first= (type(first))
    type_second = (type(second))
    if(type_first == type_second):
        result= True
    else:
        result= False
    print (result)
    return result
    pass


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    if (first is second):
        result = True
    else:
        result = False
    return result

    pass
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    pass


def multiple_ints(first_value: int, second_value: int) -> int:
   
    if((type(first_value) is int) & (type(second_value) is int)):
        return first_value * second_value
    else:
        raise TypeError
    
    pass


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    try:
        first_float = float(first_value)
        second_float = float(second_value)   
        first_int = int (first_float)
        second_int = int(second_float)
        return first_int * second_int
    except:
        raise ValueError
        
    
    pass


def is_word_in_text(word: str, text: str) -> bool:
    if (word in text):
        result = True
        return True
    else:
        result = True
        return False

    print (result)
    return result
    pass


def some_loop_exercise() -> list:
    result =[]
    for i in range(0,13):
        if ((i!=6) and (i!=7)):
            result.append(i)
    return result
    """
    if ((i!=6) & (i!=7)):
        result = [i for i in range(1,12)]
    """
    
    pass


def remove_from_list_all_negative_numbers(data: List[int]) -> list:

    result =[]
    for i in range(len(data)):
        result.append(data[i])
        if (data[i]<0):
            result.remove(data[i])
    print(result)
    return result
    
    """
    if ((i>=0)):
        result = [i for i in range(len(list)-1)]
    """
    """
a=-1000
    b=1000
    result =[]
    for i in range(len(list)-1):
        if (i>=0):
            result.append(i)
    print(result)
    """

    pass


def alphabet() -> dict:
    alph = {
        1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j', 11: 'k', 12: 'l',
        13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u', 22: 'v', 23: 'w',
        24: 'x', 25: 'y', 26: 'z'
    }
    print(alph)
    return alph 
    """
    Create dict which keys are alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    pass


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
    pass