import csv

def save_score(name, score):
    with open("SJ10-Mathbuddy-Assignment2/data/scores.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, score])

def load_scores():
    with open("data/scores.csv", "r") as file:
        reader = csv.reader(file)
        return list(reader)