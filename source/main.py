import json
import csv


if __name__ == '__main__':
    # Process to join all data and return as csv
    history = []
    for i in range(4):
        with open(f'../data/StreamingHistory{i}.json', mode='r', encoding='utf-8') as file:
            list_file = json.load(file)
            history.append(list_file)

    # unify nested list
    history = [streaming for session in history for streaming in session]

    with open('../data/streaming_history.csv', mode='w', encoding='utf-8', newline='') as file:
        w = csv.DictWriter(file, fieldnames=history[0].keys())
        w.writeheader()
        w.writerows(history)
