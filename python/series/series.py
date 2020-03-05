def slices(series, length):
    if length <= 0:
        raise ValueError("Length can't be 0 or less")
    elif length > len(series):
        raise ValueError(
                "Length must be at leat the actual length of the series"
                )
    split_series = []
    for i in range(len(series) - (length - 1)):
        split_series.append(series[i:i+length])
    return split_series
