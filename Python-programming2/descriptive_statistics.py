""" Performing Descriptive Statistical Analysis for the provided data"""

import sys
import math

# Initialized the variable to store column index

column_to_parse = int(sys.argv[2])


# Written function to define arguments and handle valueerror exception

def get_parsed_data(data, skip_number, column_number):
    """

    :param data: (list) list of integers in format of strings
    :param skip_number: (integer) defines which line in data is being parsed
    :param column_number: (integer) index number
    :return: float values of data
    """

    # Written condition if there's a null value

    if data[column_number] == "NaN":
        return None
    try:
        # Typecasting integers to floats

        floatnumber_data = float(data[column_number])

        # Skipping the line which has str value in the data

    except ValueError:
        print(f"Skipping line number {skip_number} "
              f": could not convert string to float: {data[column_number]}")
        return None
    return floatnumber_data

# Taken filepath from arguments

FILE_PATH = str(sys.argv[1])

# By using for loop stripped the data into list of numbers

# Using try/except to handle Value Error and Index error
try:
    with open(FILE_PATH, 'r', encoding="UTF-8") as infile:
        data_file = infile.readlines()
        column_data = []
        for line_number, line in enumerate(data_file):
            numbers = line.strip('\n').split("\t")
            try:
                number_data = (get_parsed_data(numbers, line_number, column_to_parse))
                if number_data is not None:
                    column_data.append(number_data)

                    # Written exception if  a values are not valid
            except ValueError:
                print("Error: There were no valid number(s) in column", sys.argv[2],
                      "in file: ", FILE_PATH.rsplit('/', maxsplit=1)[-1], file=sys.stderr)
                sys.exit(1)

                # Written exception if the column index value falls out of zone
except IndexError:
    if column_to_parse > 6:
        print("Exiting: There is no valid 'list index' in column", sys.argv[2],
              "in line 1 in file:", FILE_PATH.rsplit('/', maxsplit=1)[-1], file=sys.stderr)
        sys.exit(2)


def variance_func(extracted_data):

    """
    Written function to calculate Variance for column_data
    :param extracted_data : The column data which is indexed
    :return: Variance of the given data
    """
    deviations = [(x-Average_values)**2 for x in extracted_data]
    variance_value = sum(deviations)/len(extracted_data)
    return variance_value


def median_func(extracted_data):
    """
    Written function to calculate Median for column_data
    :param extracted_data: The column data which is indexed
    :return: Gets Median value of the provided data.
    """
    extracted_data.sort()
    if len(extracted_data)%2 == 0:
        mid_value = int(len(extracted_data)/2)
        if len(extracted_data) == 0:
            return 0
        median_value = (extracted_data[mid_value] + extracted_data[mid_value + 1])/2

    else:
        mid_value = int((len(extracted_data)+1)/2)
        if len(extracted_data) == 1:
            return extracted_data[0]
        median_value = extracted_data[mid_value]

    return median_value

if len(column_data) != 0:

    print(f"Column: {column_to_parse}", end="\n\n")

    # Printing actual number of values in a column in original file
    count = len(data_file)
    print("\tCount".ljust(10),  "=", f"{(format(round(float(count),3),'.3f'))}".rjust(10))

    # Printing Valid number of counts after exception in a column with 3 floating points
    VALID_NUM = len(column_data)
    print("\tValidNum".ljust(10), "=", f"{(format(round(float(VALID_NUM),3),'.3f'))}".rjust(10))

    # Printing Average value with 3 floating points
    Average_values = sum(column_data)/len(column_data)
    print("\tAverage".ljust(10), "=", f"{(format(round(Average_values,3),'.3f'))}".rjust(10))

    # Printing Maximum value with 3 floating points
    Maximum = max(column_data)
    print("\tMaximum".ljust(10), "=",  f"{(format(round(Maximum,3),'.3f'))}".rjust(10))

    # Printing Minimum value with 3 floating points
    Minimum = min(column_data)
    print("\tMinimum".ljust(10), "=",  f"{format(round(Minimum,3),'.3f')}".rjust(10))

    # Printing Variance value with 3 floating points
    variance = variance_func(column_data)
    print("\tVariance".ljust(10), "=", f"{format(round(variance,3),'.3f')}".rjust(10))

    # Printing StandardDeviation value with 3 floating points
    Standard_deviation = math.sqrt(variance)
    print("\tStd Dev".ljust(10), "=", f"{format(round(Standard_deviation,3),'.3f')}".rjust(10))

    # Printing Median value with 3 floating points
    Median_value = median_func(column_data)
    print("\tMedian".ljust(10), "=",  f"{format(round(Median_value,3),'.3f')}".rjust(10))
else:
    print("Error: There were no valid number(s) in column", sys.argv[2],
                      "in file: ", FILE_PATH.rsplit('/', maxsplit=1)[-1], file=sys.stderr)
