def is_nugget_number(candidate: int, sizes) -> bool:
    SMALL = sizes['S']
    MEDIUM = sizes['M']
    LARGE = sizes['L']
    for a in range(candidate//SMALL + 1):
        for b in range(candidate//MEDIUM + 1):
            for c in range(candidate//LARGE + 1):
                if candidate == a * SMALL + b * MEDIUM + c * LARGE:
                    return True
    return False

## Main
sizes = {'S' : 6, 'M' : 9, 'L' : 20}
count = 0
largest = 0
candidate = sizes['S']

while count < sizes['S']: 
    if is_nugget_number(candidate, sizes):
        count += 1
    else:
        largest = candidate
        count = 0
    candidate += 1
    
print(f"The largest number that you cannot get is: {largest}")
    
    
