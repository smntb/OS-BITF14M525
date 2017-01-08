import ProcessClass
import Queue
def main():
    processes_dictionary = {}
    quantum_time = 0
    processes_dictionary,quantum_time = get_all_processes_data(processes_dictionary,quantum_time)
    processes_dictionary = calculate_turnAround_time(processes_dictionary,quantum_time)
    display_results(processes_dictionary)

def display_results(processes_dictionary):
    for key in processes_dictionary:
        print ('Process: ',processes_dictionary[key].get_id())
        print ('Process Turn Around Time: ',processes_dictionary[key].get_turnaround_time())

def calculate_turnAround_time(processes_dictionary,quantum_time):
    ready_queue = Queue.Queue()
    total_time = 0
    running_mutex = 1
    running_process = ProcessClass.Process(-1,-1,-1)
    no_of_processes_before_ready = len(processes_dictionary)
    while no_of_processes_before_ready> 0 or ready_queue.qsize()>0 or running_process.get_id() is not -1:
        if no_of_processes_before_ready > 0:
            ready_queue,no_of_processes_before_ready,processes_dictionary,total_time = fill_ready_queue_with_current_arrived_processes(ready_queue,no_of_processes_before_ready,processes_dictionary,total_time)
        if no_of_processes_before_ready > 0 and ready_queue.qsize() == 0 and running_process.get_id()==-1:
            total_time +=1
            continue
        if running_process.get_id() == -1 and ready_queue.qsize() > 0 and running_mutex is 1:
            running_process = ready_queue.get()
            running_process.set_remaining_quantum(quantum_time)
            running_mutex = 0
        if running_process.get_id() is not -1 and running_mutex is 0:
            if running_process.get_remaining_duration()>0 and running_process.get_remaining_quantum()>0:
               total_time +=1
               running_process.set_remaining_duration((running_process.get_remaining_duration()-1))
               running_process.set_remaining_quantum((running_process.get_remaining_quantum()-1))

            if running_process.get_remaining_duration() > 0 and running_process.get_remaining_quantum() > 0:
                continue

            if running_process.get_remaining_duration() > 0 and running_process.get_remaining_quantum() ==0:
                ready_queue.put(running_process)
                running_process = ProcessClass.Process(-1,-1,-1)
                running_mutex = 1
                continue

            if running_process.get_remaining_duration() == 0 and running_process.get_remaining_quantum() > 0:
                running_process.set_turnaround_time((total_time-running_process.get_arrival_time()))
                processes_dictionary[running_process.get_id()] = running_process
                running_process = ProcessClass.Process(-1,-1,-1)
                running_mutex = 1
                continue

            if running_process.get_remaining_duration() == 0 and running_process.get_remaining_quantum() == 0:
                running_process.set_turnaround_time((total_time - running_process.get_arrival_time()))
                processes_dictionary[running_process.get_id()] = running_process
                running_process = ProcessClass.Process(-1,-1,-1)
                running_mutex = 1
    print ('Total Time: ',total_time)
    return processes_dictionary

def fill_ready_queue_with_current_arrived_processes(r_queue,no_of_processes_before_ready,processes_dict,total_time):
    for key in processes_dict:
        if processes_dict[key].get_arrival_time() == total_time and processes_dict[key]._pushed_to_ready==0:
            r_queue.put(processes_dict[key])
            processes_dict[key]._pushed_to_ready = 1
            no_of_processes_before_ready -=1
            processes_dict[key] = processes_dict[key]
    return r_queue,no_of_processes_before_ready,processes_dict,total_time

def get_all_processes_data(processes_dict,quantum):
    quantum = int(input('Enter Quantum Time: '))
    no_of_processes=int(input('Enter No of Processes: '))
    for count in range(0,no_of_processes,1):
        print ('Process: ',(count+1))
        arrival_time=int(input('Enter arrival_time: '))
        duration = int(input('Enter Duration: '))
        process = ProcessClass.Process((count+1),duration,arrival_time)
        processes_dict[(count+1)] = process
    return processes_dict,quantum
main()
