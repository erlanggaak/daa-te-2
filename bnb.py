import copy

def partition_values_from_index(values, start_index, total_value, unassigned_value,
                                test_assignment, test_value, best_assignment, best_err):
    # If start_index is beyond the end of the array,
    # then all entries have been assigned.
    if start_index >= len(values):
        # We're done. See if this assignment is better than
        # what we have so far.
        test_err = abs(2 * test_value - total_value)
        if test_err < best_err[0]:
            # This is an improvement. Save it.
            best_err[0] = test_err
            best_assignment[:] = copy.deepcopy(test_assignment)
    else:
        # See if there's any way we can assign
        # the remaining items to improve the solution.
        test_err = abs(2 * test_value - total_value)
        if test_err - unassigned_value < best_err[0]:
            # There's a chance we can make an improvement.
            # We will now assign the next item.
            unassigned_value -= values[start_index]

            # Try adding values[start_index] to set 1.
            test_assignment[start_index] = True
            partition_values_from_index(values, start_index + 1,
                                         total_value, unassigned_value,
                                         test_assignment, test_value + values[start_index],
                                         best_assignment, best_err)

            # Try adding values[start_index] to set 2.
            test_assignment[start_index] = False
            partition_values_from_index(values, start_index + 1,
                                         total_value, unassigned_value,
                                         test_assignment, test_value,
                                         best_assignment, best_err)

def main():
    files = ['kecil', 'sedang', 'besar']
    kecil = []
    sedang = []
    besar = []
    vars = [kecil, sedang, besar]

    for i, file in enumerate(files):
        with open('cases/' + file + '.in', 'r') as file:
            lines = file.readlines()

        vars[i] = [int(line.strip()) for line in lines]
        print(f'TC {files[i]}: ')
        print(vars[i])
        print()

    for i, var in enumerate(vars):
        total_value = sum(var)
        unassigned_value = total_value
        test_assignment = [False] * len(var)
        test_value = 0
        best_assignment = [False] * len(var)
        best_err = [float('inf')]

        print(f'TC {files[i]}: ')
        partition_values_from_index(var, 0, total_value, unassigned_value,
                                    test_assignment, test_value, best_assignment, best_err)
        print("Best Assignment:", best_assignment)
        print("Best Error:", best_err[0])
        print()

if __name__ == '__main__':
    main()