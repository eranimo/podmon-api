import csv, os, yaml

def get_data(file_path):
    return open(os.path.realpath('podmon/data/' + file_path))

def get_stations():
    result = {}
    with get_data('staStations.yaml') as _file:
        reader = yaml.load(_file)
        for row in reader:
            result[row['stationID']] = row
    return result


def get_types():
    result = {}
    with open(os.path.realpath('podmon/data/typeids.csv'), newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            cols = ', '.join(row)
            result[int(cols[0])] = cols[1]
    return result
