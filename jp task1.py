import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    try:
        # Load the dataset into a DataFrame
        df = pd.read_csv(file)
        return df
    except FileNotFoundError:
        print("Error: File not found. Please check the file path and try again.")
        return None
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
        return None

def exercise_1(df):
    # Check if DataFrame is not empty
    if df is not None and not df.empty:
        # Return the column names as a list
        return df.columns.tolist()
    else:
        return None

def exercise_2(df, k):
    # Check if DataFrame is not empty
    if df is not None and not df.empty:
        # Return the first k rows from the DataFrame
        return df.head(k)
    else:
        return None

# Implement the remaining functions...

def visual_1(df):
    # Transaction types bar chart
    if df is not None and not df.empty and 'type' in df.columns:
        df['type'].value_counts().plot(kind='bar')
        plt.title('Transaction Types')
        plt.xlabel('Transaction Type')
        plt.ylabel('Frequency')
        plt.show()
    else:
        print("Error: Dataset is not loaded or 'type' column does not exist.")
        if df is not None:
            print("Columns available:", df.columns.tolist())

def visual_2(df):
    # Origin account balance delta vs. Destination account balance delta scatter plot for Cash Out transactions
    if df is not None and not df.empty and 'type' in df.columns \
            and 'oldbalanceOrg' in df.columns and 'oldbalanceDest' in df.columns:
        cash_out_df = df[df['type'] == 'CASH_OUT']
        plt.scatter(cash_out_df['oldbalanceOrg'], cash_out_df['oldbalanceDest'])
        plt.title('Origin Account Balance vs. Destination Account Balance for Cash Out Transactions')
        plt.xlabel('Origin Account Balance')
        plt.ylabel('Destination Account Balance')
        plt.show()
    else:
        print("Error: Dataset is not loaded or required columns do not exist.")
        if df is not None:
            print("Columns available:", df.columns.tolist())

# Load the dataset
file_path = r"C:\Users\Shalma\project documents\transactions.csv"
df = exercise_0(file_path)

# Call the functions and print or visualize the output with error handling
if df is not None:
    print("Dataset loaded successfully.")
    print("Column Names:", exercise_1(df))
    print("First 5 Rows:")
    print(exercise_2(df, 5))
    visual_1(df)
    visual_2(df)
    # Call other functions as needed...
else:
    print("Error: Dataset is not loaded.")
