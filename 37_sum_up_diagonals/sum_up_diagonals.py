def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    first = matrix[0]
    last = matrix[-1]
    count = 0
    
    count  += first[0] + first[-1]
    count += last[0] + last[-1]
    if(len(matrix) > 2) :
        middle = matrix[int(len(matrix)/2)]
        
        count += middle[int(len(middle)/2)] *2
        return count
   
    else : 
        return count

m1 = [
             [1,   2],
            [30, 40],
         ]

print(sum_up_diagonals(m1))

m2 = [
           [1, 2, 3],
           [4, 5, 6],
     [7, 8, 9],
         ]
print(sum_up_diagonals(m2))
        