def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    merged = [intervals[0]]  # Initialize merged intervals with the first interval

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  # If the current interval overlaps with the last merged interval
            merged[-1][1] = max(merged[-1][1], interval[1])  # Merge the intervals
        else:
            merged.append(interval)  # Add the current interval to the merged list

    return merged

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))

