""" this program i wrote calculates the root of a real valued function y using binary search algorithm.
this is one of the lab exercises i did in freecodecamp python certification"""

def square_root_bisection(value, tolerance = 0.01, iterations = 50):
    if value < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if value == 0 or value == 1:
        print(f"The square root of {value} is {value}")
        return value

    
    
    if value > 1:
        low = 1
        high = value 
        
    elif value > 0 and value < 1:
        low = 0
        high = 1

    number_of_iterations = 0

    while number_of_iterations < iterations:
        mid_value = (low + high) / 2
        number_of_iterations += 1
        if mid_value ** 2  < value:
            low = mid_value
        else:
            high = mid_value
        if high - low <= tolerance:
            print(f"The square root of {value} is approximately {mid_value}")
            return mid_value
        
        
    print(f"Failed to converge within {iterations} iterations")
    return None
        
       
print(square_root_bisection(0.01, 1e-7, 50))
print(square_root_bisection(0))
print(square_root_bisection(1))
print(square_root_bisection(0.001, 1e-7, 50))
print(square_root_bisection(0.25, 1e-7, 50))
print(square_root_bisection(81, 1e-3, 50))
print(square_root_bisection(225, 1e-7, 10))