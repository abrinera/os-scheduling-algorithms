def findWaitingTime(processes, n, wt): 
	rt = [0] * n 
	for i in range(n): 
		rt[i] = processes[i][1] 
	complete = 0
	timer = 0
	minimum = 999999999
	short = 0
	check = False

	while (complete != n): 
		for j in range(n): 
			if ((processes[j][2] <= timer) and
				(rt[j] < minimum) and rt[j] > 0): 
				minimum = rt[j] 
				short = j 
				check = True
		if (check == False): 
			timer += 1
			continue

		rt[short] -= 1 
		minimum = rt[short] 
		if (minimum == 0): 
			minimum = 999999999

		if (rt[short] == 0):  
			complete += 1
			check = False
			fint = timer + 1
			wt[short] = (fint - processes[short][1] -processes[short][2]) 
			if (wt[short] < 0): 
				wt[short] = 0
		timer += 1

def findTurnAroundTime(processes, n, wt, tat): 
	for i in range(n): 
		tat[i] = processes[i][1] + wt[i] 
def findavgTime(processes, n): 
	wt = [0] * n 
	tat = [0] * n  
 
	findWaitingTime(processes, n, wt) 
	findTurnAroundTime(processes, n, wt, tat) 
 
	print("Processes   Burst Time	 Arrival Time     Waiting Time	  Turn-Around Time") 
	total_wt = 0
	total_tat = 0
	for i in range(n):
		total_wt = total_wt + wt[i] 
		total_tat = total_tat + tat[i] 
		print(" ", processes[i][0], "\t\t",processes[i][1], "\t\t",processes[i][2],"\t\t",wt[i], "\t\t", tat[i]) 

	print("\nAverage waiting time = %.4f "%(total_wt /n) ) 
	print("Average turn around time = ", total_tat / n) 

if __name__ =="__main__": 
    n = int(input('Enter no of processes: ')) 
    process = []
    for x in range(n):
        process.append([int(y) for y in input("Enter the process no, burst time, arrival time : ").split()])
    print("\nShortest Remainig Time First: \n")                       
    findavgTime(process, n)                    

 