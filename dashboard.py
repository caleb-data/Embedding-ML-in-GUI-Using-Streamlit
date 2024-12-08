import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def chatbot_dashboard():
    print("Welcome to the Customer Churn Dashboard!\n")

    # Load data
    data_file = os.path.join(os.getcwd(), "data", "train_data.csv")
    data = pd.read_csv(data_file)

    print("Data has been successfully loaded.\n")

    # Simulate sidebar filters via input
    print("Please specify filters for the data (leave blank to include all options):")
    filters = {}
    for column in ["gender", "InternetService", "Contract", "PaymentMethod"]:
        options = data[column].unique()
        print(f"\nOptions for {column}: {', '.join(map(str, options))}")
        selected = input(f"Enter your selections for {column} (comma-separated): ").split(',')
        filters[column] = [s.strip() for s in selected if s.strip()] or options.tolist()

    # Filter data based on user input
    def apply_filters(data, filters):
        for column, selected_values in filters.items():
            data = data[data[column].isin(selected_values)]
        return data

    # Plot helper for stacked bar charts
    def plot_stacked_bar(data, column, hue_column, colors, title, ylabel, filename):
        crosstab = pd.crosstab(data[column], data[hue_column], normalize="index")
        crosstab.rename({0: "Not Churned", 1: "Churned"}, axis=1, inplace=True)
        fig, ax = plt.subplots(facecolor="#f5f5f5")
        crosstab.plot(kind="bar", stacked=True, ax=ax, color=colors)
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        fig.savefig(filename)
        print(f"Generated chart: {filename}")

    # Filtered data
    filtered_data = apply_filters(data, filters)

    # Display summary
    print("\nSummary of Filtered Data:")
    print(filtered_data.describe())

    # Churn distribution
    print("\nGenerating churn distribution chart...")
    churn_counts = filtered_data["Churn"].value_counts()
    fig, ax = plt.subplots()
    ax.pie(churn_counts, labels=churn_counts.index, autopct="%1.1f%%", startangle=90, colors=["#ff9999", "#66b3ff"])
    ax.axis("equal")
    fig.savefig("churn_distribution.png")
    print("Churn distribution chart saved as 'churn_distribution.png'.")

    # Monthly charges distribution
    print("\nGenerating monthly charges distribution chart...")
    fig, ax = plt.subplots()
    sns.histplot(filtered_data["MonthlyCharges"], bins=30, kde=True, ax=ax)
    fig.savefig("monthly_charges_distribution.png")
    print("Monthly charges distribution chart saved as 'monthly_charges_distribution.png'.")

    # Scatter plot: Total Charges vs Tenure
    print("\nGenerating scatter plot: Total Charges vs Tenure...")
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_data, x="tenure", y="TotalCharges", hue="Churn", ax=ax)
    fig.savefig("scatter_tenure_vs_totalcharges.png")
    print("Scatter plot saved as 'scatter_tenure_vs_totalcharges.png'.")

    # Stacked bar charts
    print("\nGenerating stacked bar charts...")
    plot_stacked_bar(filtered_data, "Contract", "Churn", ["black", "red"], "Churn Rate by Contract Type", "Churn Rate", "contract_churn_rate.png")
    plot_stacked_bar(filtered_data, "PaymentMethod", "Churn", ["blue", "pink"], "Churn Rate by Payment Method", "Churn Rate", "payment_method_churn_rate.png")
    plot_stacked_bar(filtered_data, "InternetService", "Churn", ["lightgreen", "lightblue"], "Churn Rate by Internet Service", "Churn Rate", "internet_service_churn_rate.png")


# Run the chatbot dashboard
chatbot_dashboard()
