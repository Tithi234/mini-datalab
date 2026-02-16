from datalab.loader import load_data
from datalab.analyzer import show_summary
from datalab.cleaner import clean_missing
from datalab.visualizer import plot_column


def main():
    print("📂 Welcome to Mini DataLab")

    file_path = input("Enter CSV file path (example: data/sample.csv): ")

    df = load_data(file_path)

    if df is None:
        return

    while True:
        print("\nChoose an option:")
        print("1. View Summary")
        print("2. Clean Missing Values")
        print("3. Plot Column")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_summary(df)

        elif choice == "2":
            df = clean_missing(df)

        elif choice == "3":
            column = input("Enter column name: ")
            plot_column(df, column)

        elif choice == "4":
            print("👋 Exiting Mini DataLab.")
            break

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()

