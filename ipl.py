# libraries
import pandas as pd
import matplotlib.pyplot as plt


try:
    df = pd.read_csv("matches.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: matches.csv file not found. Make sure it's in the same folder.")
    exit()


print("First 5 rows of dataset:")
print(df.head())


print("\nColumns in dataset:")
print(df.columns)


print("\nDataset info:")
print(df.info())


if 'winner' in df.columns:
    wins = df['winner'].value_counts()

    print("\nMatch wins by teams:")
    print(wins)

    plt.figure(figsize=(10, 6))
    wins.plot(kind='bar')

    plt.title("IPL Match Winners")
    plt.xlabel("Teams")
    plt.ylabel("Number of Wins")

    plt.xticks(rotation=45)
    plt.tight_layout()

   
    plt.savefig("ipl_winners.png")

    
    plt.show()
else:
    print("'winner' column not found in dataset.")