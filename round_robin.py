def findWaitingTime(proc, n, bt, wt, quantum): 
    remaining_bt = [0] * n

    for i in range(n): 
        remaining_bt[i] = bt[i]
    t = 0 # Current time 
  
    while(1):
        allDone = True
        for i in range(n): 
            if (remaining_bt[i] > 0) :
                allDone = False
                if (remaining_bt[i] > quantum) :
                    t += quantum  
                    remaining_bt[i] -= quantum  
                else:
                    t = t + remaining_bt[i] 
                    wt[i] = t - bt[i] 
                    remaining_bt[i] = 0 
        if (allDone == True):
            break
             
def findTurnAroundTime(processes, n, bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i] 
        
def findavgTime(processes, n, bt, quantum): 
    wt = [0] * n
    tat = [0] * n  
    findWaitingTime(processes, n, bt, wt, quantum) 
    findTurnAroundTime(processes, n, bt, wt, tat) 
    print("Processe ID    Burst Time     Waiting Time    Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
 
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print(" ", i + 1, "\t\t", bt[i],"\t\t", wt[i], "\t\t", tat[i])
 
    print("\nAverage waiting time = %.5f "%(total_wt /n) )
    print("Average turn around time = %.5f "% (total_tat / n)) 
     
 
if __name__ =="__main__":
    n=int(input("Enter number of process: "))
    proc = list(map(int,input("Process ID: ").strip().split()))   
    burst_time = list(map(int,input("Burst time: ").strip().split())) 
    quantum=int(input("Enter time quantum: ")); 
    findavgTime(proc, n, burst_time, quantum)