import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

DATA_PATH = 'bp_data.csv'
CHARTS_DIR = 'charts'

# Ensure the charts directory exists
os.makedirs(CHARTS_DIR, exist_ok=True)

def add_entry(date_time, systolic, diastolic, pulse, notes):
    """Add a new BP entry to CSV."""
    entry = pd.DataFrame([{
        'DateTime': date_time,
        'Systolic': systolic,
        'Diastolic': diastolic,
        'Pulse': pulse,
        'Notes': notes
    }])
    if not os.path.exists(DATA_PATH):
        entry.to_csv(DATA_PATH, index=False)
    else:
        entry.to_csv(DATA_PATH, mode='a', header=False, index=False)

def view_data():
    """View all saved BP entries."""
    if os.path.exists(DATA_PATH):
        df = pd.read_csv(DATA_PATH)
        print(df)
    else:
        print('No data file found yet.')

def plot_trends():
    """Plot BP and Pulse trends over time."""
    if not os.path.exists(DATA_PATH):
        print('No data to plot.')
        return
    df = pd.read_csv(DATA_PATH)
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    plt.figure(figsize=(10, 6))
    plt.plot(df['DateTime'], df['Systolic'], label='Systolic')
    plt.plot(df['DateTime'], df['Diastolic'], label='Diastolic')
    plt.plot(df['DateTime'], df['Pulse'], label='Pulse')
    plt.xlabel('DateTime')
    plt.ylabel('Reading')
    plt.title('BP & Pulse Trend')
    plt.legend()
    plt.tight_layout()
    chart_path = os.path.join(CHARTS_DIR, 'bp_trend.png')
    plt.savefig(chart_path)
    plt.show()
    print(f'Chart saved to {chart_path}')

def main():
    print("Blood Pressure Tracker")
    print("1. Add New Entry")
    print("2. View Data")
    print("3. Plot Trends")
    print("4. Exit")
    while True:
        choice = input("Choose (1/2/3/4): ").strip()
        if choice == '1':
            date_time = input('DateTime (YYYY-MM-DD HH:MM): ').strip()
            systolic = int(input('Systolic: ').strip())
            diastolic = int(input('Diastolic: ').strip())
            pulse = int(input('Pulse: ').strip())
            notes = input('Notes (optional): ').strip()
            add_entry(date_time, systolic, diastolic, pulse, notes)
            print('Entry saved!\n')
        elif choice == '2':
            view_data()
        elif choice == '3':
            plot_trends()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Try again.\n')

if __name__ == '__main__':
    main()
