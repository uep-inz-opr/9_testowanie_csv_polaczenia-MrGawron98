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
    print(sorted([(int(number), numbers.count(number)) for number in set(numbers)], key = lambda x: -x[1])[0])

if __name__ == "__main__":
    main()