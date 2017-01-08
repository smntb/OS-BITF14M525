process_queue = []
finish_time=[]
wait_time = []
same_arrival_time=0
count=0
no_of_process= int(raw_input('Enter the total no of processes: '))
for input in xrange(no_of_process):
    process_queue.append([])
    process_queue[input].append(raw_input('Enter p_name: '))
    process_queue[input].append(int(raw_input('Enter p_arrival: ')))
    process_queue[input].append(int(raw_input('Enter p_bust: ')))

    process_queue[input].append(int(raw_input('Enter priority number: ')))
    print ''
    if input>0 and same_arrival_time==process_queue[input][1] :
        count+=1
    else:
        same_arrival_time = process_queue[input][1]
print 'You enter the following processes'
print 'ProcessName\tArrivalTime\tBurstTime\tPriority#'
for display in xrange(no_of_process):
    print process_queue[display][0], '\t\t\t', process_queue[display][1], '\t\t\t', process_queue[display][2],'\t\t\t',process_queue[display][3]
#if (count+1) is no_of_process:
    process_queue.sort(key=lambda process_queue: process_queue[3])


#print 'ProcessName\tArrivalTime\tBurstTime'
for display in xrange(no_of_process):
    #print process_queue[display][0], '\t\t\t', process_queue[display][1], '\t\t\t', process_queue[display][2]
    if display is 0:
        wait_time.append(0)
        finish_time.append((process_queue[display][2])+ (process_queue[display][1]))
    else:
        wait_time.append(finish_time[display - 1] - process_queue[display][1])
        finish_time.append(finish_time[display - 1] + process_queue[display][2])

print 'ProcessName\twaiting Time\tturn around Time'
for output in xrange(no_of_process):
    print process_queue[output][0], '\t\t\t', wait_time[output], '\t\t\t\t', finish_time[output] - process_queue[output][1]