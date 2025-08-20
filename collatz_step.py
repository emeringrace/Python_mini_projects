def steps(number):
    
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Only positive numbers are allowed")

    step_count = 0

    while number != 1:
        if number % 2 == 0:  # Number is even
            number //= 2
        else:  # Number is odd
            number = 3 * number + 1
        step_count += 1

    return step_count
