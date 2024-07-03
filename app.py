def solution(N):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    max_unique_letters = min(26, N)
    

    for k in range(max_unique_letters, 0, -1):
        if N % k == 0:
            num_repeats = N // k
            break
    

    result = ''.join(alphabet[:k] * num_repeats)
    
    return result


print(solution(3))   
print(solution(5))   
print(solution(30))  