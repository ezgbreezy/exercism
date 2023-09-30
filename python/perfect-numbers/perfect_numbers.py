def classify(number: int) -> str:
    """ 
    Classifies perfect numbers. 

    A perfect number equals the sum of its positive divisors.

    :param number: int - a positive integer
    :return: str - the classification of the input integer
    """
    
    # Check if arg is positive integer
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    # Get factors
    factors = []
    for factor in range(1, number):
        if number % factor == 0:
            factors.append(factor)
    factor_sum = sum(factors)

    print(factor_sum, number)
    if factor == number:
        print('equal')
        
    # Check classification
    match factor_sum:
        case 100:
            return 100
        case number:
            return 'number'
        #case factor_sum if factor_sum == number:
        #    return "perfect"
        #case factor_sum if factor_sum > number:
        #    return "abundant"
        #case factor_sum if factor_sum < number:
        #    return "deficient"