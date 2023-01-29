def first_come_first_served(processes):
    n = len(processes)
    waiting_time = 0
    turn_around_time = 0
    
    for i in range(n):
        if i == 0:
            waiting_time = 0
        else:
            waiting_time = waiting_time + processes[i-1][2]
        
        turn_around_time = waiting_time + processes[i][2]
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

# example input
processes = [[1, 0, 8], [2, 1, 4], [3, 2, 9]]
first_come_first_served(processes)
