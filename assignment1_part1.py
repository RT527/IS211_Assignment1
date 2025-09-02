#Rafi Talukder
class ListDivideException(Exception):
    pass #Exception Class
def list_divide(numbers, divide=2): #default  value for divid is 2
    """The function returns the number of elements in the numbers list that are divisibleby divide"""
    if divide == 0:
        raise ListDivideException("Oops, we can't divide by zero")

    count = 0
    for number in numbers:   #This parses through the numbers within the list
        if number % divide == 0:   # The function returns the number of elements in the numbers list that are divisibleby divide"""
            count += 1   # This increments the count when the requirement (number % divide == 0) is satisfied
    return count # This returns the count after the for loop is done

def test_list_divide():
    try:
        assert list_divide([1,2,3,4,5]) == 2
        assert list_divide([2,4,6,8,10]) == 5
        assert list_divide([30, 54, 63,98, 100], divide=10) == 2
        assert list_divide([]) == 0
        assert list_divide([1,2,3,4,5], 1) == 5
    except AssertionError as e:
        raise ListDivideException("Failed test case sorry") from e
    # Custom exception for 0
    try:
        list_divide([1,2,3], 0)
    except ListDivideException as e:
        print(f"Expected exception {e}")
    else:
        print("Expected ListDivideException, nothing raised")
        assert False
    
if __name__ == "__main__":
    test_list_divide()
    print("All tests have passed and are completed =)")
