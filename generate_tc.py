import random
import os

def generate_random(n):
    data = []
    for i in range(n):
        d = random.randint(1, 100)
        if d not in data:
            data.append(d)
    return data

def generate_cases():
    # Generate the testcases
    tc = {
        'kecil' : generate_random(10),
        'sedang' : generate_random(40),
        'besar' : generate_random(80),
    }
    print(tc)
    return tc

def generate():
    # Generate the testcases
    tc = generate_cases()

    # Create the directory if it doesn't exist
    TC_DIR = './cases/'

    if not os.path.exists(TC_DIR):
        os.makedirs(TC_DIR)

    # Save the testcases to files
    for name, testcase in tc.items():
        file_path = TC_DIR + str(name) + '.in'
        with open(file_path, 'w') as file_input:
            for num in testcase:
                file_input.write(str(num) + '\n')

    return tc

def tc_to_list():
    files = ['kecil', 'sedang', 'besar']
    kecil = []
    sedang = []
    besar = []
    vars = [kecil, sedang, besar]
    tc_dict = {}

    for i, file in enumerate(files):
        with open('cases/' + file + '.in', 'r') as file:
            lines = file.readlines()

        vars[i] = [int(line.strip()) for line in lines]
        tc_dict[files[i]] = vars[i]

    return tc_dict

def main():
    generate()
    tc_to_list()