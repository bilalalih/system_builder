# This is a script that loads a csv, prints summary and saves cleaned csv
import pandas as pd
import os

# Function that gets the file path from the user
def get_file_path():
    while True:
        path = input("Enter file path: ").strip() #removes excess space
        if os.path.isfile(path): # Checks if the file exists
            return path
        print("Invalid file path. Try again.")

# This Function loads the dataset using path
def load_path(path):
    try:
        df = pd.read_csv(path)
        return df
    except pd.errors.EmptyDataError:
        print("CSV is empty! Try another")
        return None
    except pd.errors.ParserError:
        print("CSV parsing error! Try another")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# This function fills missing values in the data
def fill_na(df):
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col].fillna(df[col].median())
        elif df[col].dtype == 'bool':
            df[col].fillna(False)
        else:
            df[col].fillna("Unknown")
    return df

# This function asks the user for the path to save the file
def save_file_path():
    while True:
        path = input("Enter save path(with.csv): ").strip()
        dir = os.path.dirname(path)
        if path.endswith('.csv') and (dir == '' or os.path.isdir(dir)):
            return path
        print("Invalid path. Check dir or .csv.")

# This function saves the file
def save_file(df, path, retries=2):
    for _ in range(retries):
        try:
            df.to_csv(path, index=False)
            print(f"Saved to {path}")
            return
        except Exception as e:
            print(f"Error: {e}. Retrying...")
    print("Failed to save.")

while True: # A loop that'll keep running
    data = get_file_path()
    df = load_path(data)
    if df is not None:
        df = fill_na(df)# This line prints out a statistical summary of our dataframe
        print(df.describe())
        pt = save_file_path()
        save_file(df, pt)
        cont = input("Process another file? (y/n): ").lower()
        if cont != 'y':
            break
    else:
        break