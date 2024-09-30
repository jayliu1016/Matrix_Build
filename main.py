import pandas as pd
import matplotlib.pyplot as plt

# Load the player overview dataset
soccer_df = pd.read_csv("player_overview.csv")


# print the head of the dataset to showcase what variables it includes
def print_head():
    soccer_head = soccer_df.head()
    print(soccer_head)
    return soccer_head


# describe the dataset's statistics for all numerical columns
def describe_stat():
    # This will include statistics like mean, median, std for all numerical columns
    soccer_desc = soccer_df.describe(include=[float, int])
    print(soccer_desc)
    return soccer_desc


# create a scatter plot of the 'Goals' and 'Assists' columns
def build_scatter_plot():
    plt.scatter(soccer_df['Goals'], soccer_df['Assists'], alpha=0.6, color='blue')
    plt.xlabel('Goals')
    plt.ylabel('Assists')
    plt.title('Scatter Plot of Goals vs Assists')
    plt.savefig("Goals_Assists_Scatter.png")
    plt.show()


# main to execute the functions
if __name__ == "__main__":
    print_head()
    describe_stat()
    build_scatter_plot()
