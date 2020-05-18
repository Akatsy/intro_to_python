def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n+5 for n in num_list]

if __name__ == '__main__':
    print("Testing functions")
    n_list = [10, 20, 40, 60, 80]
    correct_mean  = 42
    assert(mean(n_list) == correct_mean)

    correct_added_list = [15, 25, 45, 65, 85]
    assert(add_five(n_list) == correct_added_list)

    print("Tests passed!")
