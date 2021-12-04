from typing import List


def ReadFile(FilePath):
    with open(FilePath) as File:
        Lines = File.read().splitlines()
    return Lines

binary_count_list = []

def count_binary(input):
    if len(binary_count_list) == 0:
        initialize_list(input)

    input_char_list = list(input)

    for index, binary_char in enumerate(input_char_list):
        binary_count_list[index] += 1 if int(binary_char) == 1 else -1

def initialize_list(string):
    global binary_count_list
    binary_count_list = [0] * len(string)

def getGamma():
    gamma = ""
    for binary_count in binary_count_list:
        gamma += "1" if binary_count > 0 else "0"
        if binary_count == 0:
            print("ERROR EQUAL COUNT!!!!!!!")
    return gamma

def getepsilon():
    epsilon = ""
    for binary_count in binary_count_list:
        epsilon += "0" if binary_count > 0 else "1"
        if binary_count == 0:
            print("ERROR EQUAL COUNT!!!!!!!")
    return epsilon

def Main():
    log_lines = ReadFile('D:\Tools\input_Day3.txt')
    for line in log_lines:
        count_binary(line)
    gamma = getGamma()
    epsilon = getepsilon()
    decimal_gamma = int(gamma,2)
    decimal_epsilon = int(epsilon,2)
    print("Binary Epsilon: " + epsilon + "\nBinary Gamma: " + gamma + "\nDecimal Epsilon: " + str(decimal_epsilon) + "\nBinary Gamma: " + str(decimal_gamma) + "\n TotalSum: " + str(decimal_gamma * decimal_epsilon))

Main()