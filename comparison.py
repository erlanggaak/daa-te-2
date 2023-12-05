import time
import bnb
import dp
import generate_tc
from memory_profiler import profile

def setup():
    tc_dict = generate_tc.tc_to_list()
    return tc_dict

def count_execution_time(start, end):
    return (end - start) * 1000

def execute_dp(arr, title):
    print(f'{title} ')

    # Count Execution Time for DP
    start_time = time.time()
    dp.findPartition(arr, len(arr)) 
    end_time = time.time()
    execution_time = count_execution_time(start_time, end_time)
    print("Execution Time DP: {:.4f} ms".format(execution_time))
    print()

def execute_bnb(arr, title):
    print(f'{title} ')

    total_value = sum(arr)
    unassigned_value = total_value
    test_assignment = [False] * len(arr)
    test_value = 0
    best_assignment = [False] * len(arr)
    best_err = [float('inf')]

    # Count Execution Time for DP
    start_time = time.time()
    bnb.partition_values_from_index(arr, 0, total_value, unassigned_value,
                                    test_assignment, test_value, best_assignment, best_err)
    end_time = time.time()
    execution_time = count_execution_time(start_time, end_time)
    print("Execution Time DP: {:.4f} ms".format(execution_time))
    print()

@profile
def main():
    tc = setup()
    kecil = tc.get('kecil')
    sedang = tc.get('sedang')
    besar = tc.get('besar')

    execute_dp(kecil, 'TC Kecil DP:')
    execute_dp(sedang, 'TC Sedang DP:')
    execute_dp(besar, 'TC Besar DP:')

    print('===========================================')
    
    execute_bnb(kecil, 'TC Kecil BnB:')
    execute_bnb(sedang, 'TC Sedang BnB:')
    # execute_bnb(besar, 'TC Besar BnB:')

if __name__ == "__main__":
    main()
