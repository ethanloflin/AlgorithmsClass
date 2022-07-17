def fractionalknapsack(values,weights,Total_capacity):
    n = len(values)

    def score(i) : return values[i]/weights[i]

    items = sorted(range(n)  , key=score , reverse = True)
    sel, value,weight = [],0,0
    for i in items:
        if weight +weights[i] <= capacity:
            sel += [i]
            weight += weights[i]
            value += values [i]
    return value
