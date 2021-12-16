import matplotlib.pyplot as plt
import pandas as pd

sleep_data = pd.read_csv("Sleep Data.csv")
sleep_data_df = pd.DataFrame(sleep_data)

def days_graph(day_of_week, graph_label, title):
    hours_slept_data = []
    day_of_week_dates = []
    index_list = []
    small_index = []
    small_day_of_week_dates = []
    for x in range(len(sleep_data)):
        if (day_of_week == sleep_data.at[x, "Day"]):
            hours_slept_data.append(sleep_data.at[x, "Total Time Slept (H)"])
            day_of_week_dates.append(sleep_data.at[x, "Date"])
            index_list.append(x)
    for x in range(0,len(day_of_week_dates),2):
        small_index.append(index_list[x])
        small_day_of_week_dates.append(day_of_week_dates[x])
    y = list(range(len(hours_slept_data)))
    plt.figure()
    plt.bar(index_list, hours_slept_data, facecolor="blue", edgecolor="black", label=graph_label, width=6)
    plt.xticks(small_index, small_day_of_week_dates, rotation=45, ha="right")
    plt.yticks(list(range(10)))
    plt.xlabel("Date")
    plt.ylabel("Total Time Slept (H)")
    plt.title(title)
    plt.legend()
    plt.show()



def create_bar_graph(list_numbers, graph_label, title, filename):
    dates_list = []
    index_list = []
    small_index = []
    small_dates = []
    x = list(range(len(list_numbers)))
    plt.figure()
    
    for y in range(len(list_numbers)):
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
    #plt.savefig(filename)
    #print("Dates List:", dates_list)
    #print("Index List:", index_list)
    print("Small Index:", small_index)
    print("small_dates", small_dates)


def weekend_graph(list_of_data, x_label, title, filename):

    weekend_sleep = []
    weekday_sleep = []
    weekend_sleep_dates = []
    weekday_sleep_dates = []

    for x in range(len(sleep_data)):
        if ("Friday" in sleep_data.at[x, "Day"] or "Saturday" in sleep_data.at[x, "Day"]):
            weekend_sleep.append(sleep_data.at[x, "Total Time Slept (H)"])
            weekend_sleep_dates.append(sleep_data.at[x,"Date"])

    for x in range(len(sleep_data)):
        if ("Sunday" in sleep_data.at[x, "Day"] or "Monday" in sleep_data.at[x, "Day"] or "Tuesday" in sleep_data.at[x, "Day"] or "Wednesday" in sleep_data.at[x, "Day"] or "Thursday" in sleep_data.at[x, "Day"]):
            weekday_sleep.append(sleep_data.at[x, "Total Time Slept (H)"])
            weekday_sleep_dates.append(sleep_data.at[x,"Date"])

    x = list(range(len(list_of_data)))
    plt.figure()
    graph_label = "Total Time Slept (H)"
    plt.bar(x, list_of_data, facecolor="red", edgecolor="black", label=graph_label)
    #plt.xticks([weekend_sleep_dates])
    plt.yticks([0,9])
    plt.xlabel(x_label)
    plt.ylabel("Total Time Slept (H)")
    plt.title(title)
    plt.legend()
    plt.show()
    #plt.savefig(filename)

 
