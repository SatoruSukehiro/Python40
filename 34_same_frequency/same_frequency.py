def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_list1 = [x for x in str(num1)]
    num_list2 = [x for x in str(num2)]

    num_list1.sort()
    num_list2.sort()
   

    if num_list1 ==  num_list2 :
        return True
    else:
        return False


print(same_frequency(7111777,1777111))