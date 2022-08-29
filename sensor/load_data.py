import glob
import os
import csv


def load_sensor_data():
    """Load the sensor dta from csv."""
    sensor_data = []
    current_dir = os.getcwd()
    datasets_dir = "datasets"
    if current_dir.endswith('\\sensor'):
        datasets_dir = f"..\\{datasets_dir}"
    sensor_files = glob.glob(os.path.join(os.getcwd(), datasets_dir, '*.csv'))
    for sensor_file in sensor_files:
        with open(sensor_file) as data_file:
            data_reader = csv.DictReader(data_file, delimiter=',')
            for row in data_reader:
                sensor_data.append(row)
    return sensor_data


if __name__ == "__main__":
    load_sensor_data()
