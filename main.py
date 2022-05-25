import csv

def main():
    numbers = []
    with open("phoneCalls.csv") as file:
        csv_reader = csv.reader(file, delimiter = ",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                numbers.append(row[0])
    numbers_set = set(numbers)
    result = []
    for number in numbers_set:
        result.append((number, numbers.count(number)))
    result = sorted(result, key = lambda x: -x[1])
    max = result[0]
    print(max)

if __name__ == "__main__":
    main()