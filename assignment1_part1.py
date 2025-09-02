
def list_divide(numbers, divide):
    """The function returns the number of elements in the numbers list that are divisibleby divide"""
    count = 0
    for number in numbers:   #This parses through the numbers within the list
        if number % divide == 0:   # The function returns the number of elements in the numbers list that are divisibleby divide"""
            count += 1   # This increments the count when the requirement (number % divide == 0) is satisfied
    return count # This returns the count after the for loop is done

class ListDivideException(Exception):
    pass #Exception Class

def test_list_divide():
    assert list_divide([1,2,3,4,5]) == 2
    assert list_divide([2,4,6,8,10]) == 5
    assert list_divide([30, 54, 63,98, 100], divide=10) == 2
    assert list_divide([]) == 0
    assert list_divide([1,2,3,4,5], 1) == 5
    
if __name__ == "__main__":
    test_list_divide()
