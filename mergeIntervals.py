
def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    current_interval = sortedIntervals[0]
    output_arr = [current_interval]

    for i in range(len(sortedIntervals) -1):

        current_begin = sortedIntervals[i][0]
        current_end = sortedIntervals[i][1]
        next_begin = sortedIntervals[i+1][0]
        next_end = sortedIntervals[i+1][1]
        if current_end >= next_begin:
            current_interval[1] = max(current_end, next_end)
        else:
            current_interval = sortedIntervals[i+1]
            output_arr.append(current_interval)
    return output_arr
intervals = [[2,6], [1,3], [8,10], [15,18]]
output = merge(intervals)