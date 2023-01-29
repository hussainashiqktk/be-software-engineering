import matplotlib.pyplot as plt
import pandas as pd

def gantt_chart(processes):
    n = len(processes)
    waiting_time = 0
    turn_around_time = 0
    gantt = []
    
    processes = sorted(processes, key=lambda x: x[2])
    
    for i in range(n):
        if i == 0:
            waiting_time = 0
        else:
            waiting_time = waiting_time + processes[i-1][2]
        
        turn_around_time = waiting_time + processes[i][2]
        gantt.append([processes[i][0], waiting_time, turn_around_time])
        
        print("Process ID: ", processes[i][0])
        print("Arrival Time: ", processes[i][1])
        print("Burst Time: ", processes[i][2])
        print("Waiting Time: ", waiting_time)
        print("Turn Around Time: ", turn_around_time)
        print()
        
    avg_waiting_time = waiting_time / n
    avg_turn_around_time = turn_around_time / n
    print("Average Waiting Time: ", avg_waiting_time)
    print("Average Turn Around Time: ", avg_turn_around_time)
    print("Gantt Chart: ", gantt)
    
    df = pd.DataFrame(gantt, columns=["Process ID", "Waiting Time", "Turnaround Time"])
    print("\nTurnaround Times:")
    print(df)
    
    x = [p[0] for p in gantt]
    y = [p[1] for p in gantt]
    height = [p[2] - p[1] for p in gantt]
    
    plt.barh(x, height, left=y, color='blue', alpha=0.7)
    plt.title("Gantt Chart")
    plt.xlabel("Time")
    plt.ylabel("Process ID")
    plt.xticks(range(0, max(y)+max(height), 1))
    
    plt.show()

# example input
processes = [["P1", 2, 2], ["P2", 1, 1], ["P3", 8, 4], ["P4", 4, 2], ["P5", 5, 3]]
gantt_chart(processes)
