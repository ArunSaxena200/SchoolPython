def mergeIntervals(intervals):
    '''
    [1,3],[2,6],[8,10]
    1,6
    3>2, max(3,6)
    '''
    intervals = sorted(intervals, key= lambda x:x[0])
    current_interval = intervals[0]
    mergedInterval = []
    mergedInterval.append(current_interval)
    for next_intervals in intervals:
        _,current_interval_end = current_interval
        next_intervals_start,next_intervals_end = next_intervals
        if current_interval_end>next_intervals_start:
            current_interval[1]=max(current_interval_end,next_intervals_end)
        else:
            current_interval = next_intervals
            mergedInterval.append(current_interval)
    return mergedInterval

print(mergeIntervals([[1,3],[2,6],[15,18],[8,10]]))
