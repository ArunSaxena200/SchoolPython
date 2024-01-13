def weighted_average(numbers, weights):

    if len(numbers) != len(weights):

        raise ValueError("Length of numbers and weights should be the same")

    total_weighted_sum = sum(x * w for x, w in zip(numbers, weights))
    print(total_weighted_sum)

    total_weight = sum(weights)

    print(total_weighted_sum,total_weight)
    if total_weight == 0:

        raise ValueError("Total weight should be greater than 0")
    

    return total_weighted_sum / total_weight

data_list = [10, 15, 20, 25, 30]

weights = [0.1, 0.2, 0.3, 0.2, 0.29]

weighted_avg = weighted_average(data_list, weights)

print("Weighted Average:", weighted_avg)