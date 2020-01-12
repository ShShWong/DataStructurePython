def sequentialSearch(target,lyst):
    '''
        顺序搜索
    '''
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1
    return -1

lyst = "google"
print(sequentialSearch('a',lyst))
            