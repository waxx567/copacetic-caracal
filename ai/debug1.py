'''
Your colleague has written a simple statistical analysis function in Python to calculate the number of occurrences of each item in a dataset. The function is expected to perform efficiently, ideally with O(n) time complexity. However, something went wrong, leading to unintended poor performance (far worse than linear complexity).
'''
def calculate_occurrences(items):
    occurrences = {}
    for item in items:
        if item in occurrences:
            occurrences[item] += 1
        else:
            occurrences[item] = 1
    return occurrences

items = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
result = calculate_occurrences(items)
print(result)