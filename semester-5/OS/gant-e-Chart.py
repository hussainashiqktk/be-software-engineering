import matplotlib.pyplot as plt

def gantt_chart(processes):
    n = len(processes)
    waiting_time = 0
    turn_around_time = 0
    gantt = []
    
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
    
    y = [p[0] for p in gantt]
    xmin = [p[1] for p in gantt]
    xmax = [p[2] for p in gantt]
    plt.hlines(y=y, xmin=xmin, xmax=xmax, color='blue', alpha=0.7)
    plt.vlines(x=xmin, ymin=0, ymax=y, color='gray', alpha=0.7)
    plt.vlines(x=xmax, ymin=0, ymax=y, color='gray', alpha=0.7)
    
    plt.title("Gantt Chart")
    plt.xlabel("Time")
    plt.ylabel("Process ID")
    plt.yticks(y)
    
    plt.show()
    
# example input
processes = [[1, 0, 8], [2, 1, 4], [3, 2, 9]]
gantt_chart(processes)
