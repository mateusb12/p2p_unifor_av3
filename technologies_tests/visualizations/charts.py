import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from path_references.all_references import get_merged_csv_path


def get_merged_df() -> pd.DataFrame:
    file_path = get_merged_csv_path()
    data = pd.read_csv(file_path)
    data['Failure Rate'] = (data['Failure Count'] / data['Request Count']) * 100
    return data[data['Name'] != 'Aggregated']


class Visualization:
    def __init__(self):
        self.data = get_merged_df()

    def average_response_by_technology(self):
        plt.figure(figsize=(10, 6))  # Adjust figure size if necessary
        sns.barplot(x="Technology", y="Average Response Time", data=self.data)  # Ensure 'Technology' is a column in self.data
        plt.title("Average Response Time by Technology")
        plt.ylabel("Average Response Time (ms)")
        plt.xlabel("Technology")
        plt.xticks(rotation=45, ha="right", fontsize='x-small')  # Adjust fontsize if necessary
        plt.tight_layout()  # This will adjust the plot to ensure everything fits without overlap
        plt.grid(True)

    def failure_rate_by_technology(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Technology", y="Failure Rate", data=self.data)
        plt.title("Failure Rate by Technology")
        plt.ylabel("Failure Rate (%)")
        plt.xlabel("Technology")
        plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
        plt.grid(True)

    def request_count_by_technology(self):
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Technology", y="Request Count", data=self.data)
        plt.title("Request Count by Technology")
        plt.ylabel("Request Count")
        plt.xlabel("Technology")
        plt.xticks(rotation=45, ha="right")  # Rotate x-axis labels for better readability
        plt.grid(True)


def __main():
    df = get_merged_df()
    v = Visualization()
    v.average_response_by_technology()
    v.failure_rate_by_technology()
    v.request_count_by_technology()
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    __main()
