def arrange_guest_arrival_order(arrival_pattern):
    numbers = []
    result = []

    for i, char in enumerate(arrival_pattern):
        numbers.append(i + 1)
        if char == 'I':
            while numbers:
                result.append(numbers.pop())
                # numbers = [4, 6, 7, 8]
                # result = [1, 2, 3, 5]
        
    numbers.append(len(arrival_pattern) + 1)

    while numbers:
        result.append(numbers.pop())
        # [1, 2, 3, 5, 4, 8, 7, 6]
        # 12354876

    return "".join(str(x) for x in result)

    
    
print(arrange_guest_arrival_order("IIIDIDDD"))
print(arrange_guest_arrival_order("DDD"))
