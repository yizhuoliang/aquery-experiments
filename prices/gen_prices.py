import csv
import random

# Number of lines
num_lines = 10000000

# Generate months in random order
months = list(range(1, num_lines + 1))
random.shuffle(months)

# Generate random prices
prices = [random.randint(1, 2000) for _ in range(num_lines)]

# Write to CSV file
with open('prices.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['month', 'price'])  # Write header
    for month, price in zip(months, prices):
        csvwriter.writerow([month, price])

print(f"CSV file with {num_lines} lines generated as 'output.csv'")
