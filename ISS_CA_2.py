def find_cube_pairs(targ): # target changed to targ, : added
    sol = []; # solutions changed to sol
    max_num = round(targ ** (1/3)) # 3 * changed to 2 *

    for a in range(1, max_num + 1): # : added, changed ranges to range
        for b in range(a, max_num + 1): # : added, changed ranges to range
            if a**3 + b**3 == targ: # 3 * changed to 2 * and : added
                sol.append((a, b)) # removed semicolon, though it doesn't produce an error even if the semicolon is still there. 
    return sol

pairs = find_cube_pairs(1729) # commas removed
print("Valid cube pairs for 1729:") # comma removed, string changed to reflect input, printf changed to print
for a, b in pairs: # pair changedd to pairs, : added
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729") # printf changed to print, a**2 changed to a**3, and b**2 changed to b**3, 1728 changed ot 1729 to reflect input
