import csv

def save_score(name, score):
    with open("data/scores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, score])