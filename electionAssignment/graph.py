import matplotlib.pyplot as plt
import pandas as pd

def graph(file):
    """
    Creates a new window displaying a bar graph

    Args:
        file (str): a string saying the name of the file that should be opened
    """
    data = pd.read_csv(file+".csv")                                        # use pandas function to read the csv
    df = pd.DataFrame(data)                                         # convert the previously opened csv data into a pandas DataFrame

    # I have no clue what this does but it is probally some wierd magic to reshape dataframe
    x = list(df.iloc[:,0])
    y = list(df.iloc[:,1])


    plt.bar(x,y)                                                    # Create the bar graph
    plt.title(f"Top used words used in {file}")                     # Edit title for the graph
    plt.xlabel('Words')                                             # X label name
    plt.ylabel("Number of times used")                              # Y label name

    plt.show()                                                      # Accualy show the graph