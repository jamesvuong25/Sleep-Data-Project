import matplotlib.pyplot as plt


def create_bar_graph(list_numbers, graph_label, title, filename):
    dates_list = []
    index_list = []
    small_index = []
    small_dates = []
    x = list(range(len(list_numbers)))
    plt.figure()
    
    for y in range(len(sleep_data)):
        dates_list.append(sleep_data.at[y, "Date"])
        index_list.append(y)

    for y in range(0,len(dates_list), 8):
        small_index.append(index_list[y])
        small_dates.append(dates_list[y])

    plt.bar(x, list_numbers, facecolor="blue", edgecolor="black", label=graph_label)
    plt.xticks(small_index,small_dates,rotation=45,ha="right")
    plt.yticks(list(range(10)))
    plt.xlabel("Date")
    plt.ylabel("Total Time Slept (H)")
    plt.title(title)
    plt.legend()
    plt.show()
    plt.savefig(filename)
    #print("Dates List:", dates_list)
    #print("Index List:", index_list)
    print("Small Index:", small_index)
    print("small_dates", small_dates)