def ReadFile(FilePath):
    with open(FilePath) as File:
        Lines = File.read().splitlines()
    return Lines



def get_most_least_common(log_lines, char_index, most_bool, filter_string):
    binary_counter = 0
    last_match_counter = 0
    last_match = ""

    most_filter_binary = "1" if most_bool else "0"
    least_filter_binary = "0" if most_bool else "1"

    for log_line in log_lines:
        if not log_line.startswith(filter_string):
            continue
        log_line_char = list(log_line)
        binary_counter += 1 if int(log_line_char[char_index]) > 0 else -1
        last_match_counter+=1
        last_match = log_line
    
    if(last_match_counter == 1):
        return last_match

    if binary_counter >= 0:
        return filter_string + most_filter_binary
    else:
        return filter_string + least_filter_binary

#oxygen_or_co2 = true for oxygen, oxygen_or_co2 = false for co2
def get_oxygen_or_co2(log_lines, oxygen_or_co2):
    char_index = 0
    filter_string = ''
    while True:
        filter_string = get_most_least_common(log_lines,char_index,oxygen_or_co2,filter_string)
        if len(filter_string) == len(log_lines[0]):
            break
        char_index+=1
    return filter_string

def main():
    log_lines = ReadFile(r'D:\Tools\input_Day3.txt')
    oxygen = get_oxygen_or_co2(log_lines, True)
    co2 = get_oxygen_or_co2(log_lines,False)
    decimal_oxygen = int(oxygen,2)
    decimal_co2 = int(co2, 2)
    print("Binary oxygen: " + oxygen + "\nBinary co2: " + co2 + "\nDecimal oxygen: " + str(decimal_oxygen) + "\nBinary co2: " + str(decimal_co2) + "\n TotalSum: " + str(decimal_co2 * decimal_oxygen))

main()
