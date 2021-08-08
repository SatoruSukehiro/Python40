def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """
    str_list = [str(num) for num in nums]
    check = { num : str_list.count(num) for num in str_list}
    values = set(check.values())
    if len(values) > 1 :
    
        return max(check, key = check.get)
    else:  return True
    
  
        
    

print(find_the_duplicate([2, 1, 3, 4]))

print(find_the_duplicate([1, 2, 1, 4, 3, 12]))
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))