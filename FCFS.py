def WaitingTime(processes, n, bt, wt, at):
    service_time = [0] * n  
    service_time[0] = 0
    wt[0] = 0
   
    for i in range(1, n):  
        service_time[i] = (service_time[i - 1] + bt[i - 1])  # Add burst time of previous processes  
        wt[i] = service_time[i] - at[i]  
  
        if (wt[i] < 0): 
            wt[i] = 0 
 
def TurnaroundTime(processes, n, bt, wt, tr):    
    for i in range(n): 
        tr[i] = bt[i] + wt[i]  
    
def AvgTime(processes, n, bt, at):  
    wt = [0] * n 
    tr = [0] * n  
    WaitingTime(processes, n, bt, wt, at)    
    TurnaroundTime(processes, n, bt, wt, tr)  
    print("\nFirst come first serve: \n")
    print("Processes   Burst Time   Arrival Time     Waiting Time",  
          "Turn-Around Time  Completion Time \n") 
    total_wt = 0
    total_tr = 0
    for i in range(n): 
  
        total_wt = total_wt + wt[i]  
        total_tr = total_tr + tr[i]  
        compl_time = tr[i] + at[i]  
        print(" ", i + 1, "\t\t", bt[i], "\t\t", at[i],"\t\t",
              wt[i], "\t\t ", tr[i], "\t\t ", compl_time)  
  
    print("Average waiting time = %.3f "%(total_wt /n)) 
    print("\nAverage turn around time = ", total_tr / n)  
  
if __name__ =="__main__": 
    n=int(input("Enter number of process: "))
    processes = list(map(int,input("Process ID: ").strip().split()))   
    burst_time = list(map(int,input("Burst time: ").strip().split()))
    arrival_time = list(map(int,input("Arrival time: ").strip().split()))

    # sorting
    for i in range(len(arrival_time)):
        min=i
        for j in range (i+1,len(arrival_time)):
            if arrival_time[min]>arrival_time[j]:
                swap=True
                min=j
            else:
                swap=False     
       
        arrival_time[i],arrival_time[min]=arrival_time[min],arrival_time[i]
        for i in range(len(burst_time)):
            min=i
            for j in range(i+1,len(burst_time)):
                if swap==True:
                    min=j
            burst_time[i],burst_time[min]=burst_time[min],burst_time[i]
    AvgTime(processes, n, burst_time, arrival_time) 