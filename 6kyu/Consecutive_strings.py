def longest_consec(strarr, k):
    if k <= 0 or len(strarr) == 0 or k > len(strarr):
        return ""
    
    res = []
    range_of_loop = len(strarr)-k+1
    for i in range(range_of_loop):
        res.append("".join(strarr[i:i+k]))
    
    res.sort(key = len, reverse = True)
    return res[0]