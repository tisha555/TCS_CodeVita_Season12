def count_valid_combinations(trees):
    n = len(trees)
    count = 0
    
    
    count_M_before = 0  
    count_L_before = 0  
    
    
    for i in range(n):
        if trees[i] == 'M':
            
            count += count_L_before * (count_L_before - 1) // 2
            count_M_before += 1
        elif trees[i] == 'L':
            
            count += count_M_before * (count_M_before - 1) // 2
            count_L_before += 1
            
    
    count_M_after = 0  
    count_L_after = 0  
    
    
    for i in range(n - 1, -1, -1):
        if trees[i] == 'M':
            count += count_L_after * (count_L_after - 1) // 2
            count_M_after += 1
        elif trees[i] == 'L':
            count += count_M_after * (count_M_after - 1) // 2
            count_L_after += 1
            
    return count

def find_winner(row_ashok, row_anand):
    
    if not all(c in 'ML' for c in row_ashok) or not all(c in 'ML' for c in row_anand):
        return "Invalid input"
    
   
    count_ashok = count_valid_combinations(row_ashok)
    count_anand = count_valid_combinations(row_anand)
    
    
    if count_ashok > count_anand:
        return "Ashok"
    elif count_anand > count_ashok:
        return "Anand"
    else:
        return "Draw"


ashok_row = input().strip()
anand_row = input().strip()


print(find_winner(ashok_row, anand_row), end = '')
