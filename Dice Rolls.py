def solution(A, F, M):
    total_rolls = len(A) + F

    total_sum_needed = M * total_rolls
    
    current_sum = sum(A)
    
    forgotten_sum_needed = total_sum_needed - current_sum
      
    if forgotten_sum_needed < F or forgotten_sum_needed > 6 * F:
        return [0]

    result = [1] * F
    
    forgotten_sum_needed -= F
    

    for i in range(F):
        add_value = min(5, forgotten_sum_needed)
        result[i] += add_value
        forgotten_sum_needed -= add_value
    
    return result
print(solution([3, 2, 4, 3], 2, 4))  
print(solution([1, 5, 6], 4, 3))     
print(solution([1, 2, 3, 4], 4, 6))  
print(solution([6, 1], 1, 1))        