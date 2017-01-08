class Process:
    def __init__(self,id,duration,arrival_time):
        self.__id=id
        self.__duration=duration
        self.__remaining_duration = self.__duration
        self.__remaining_quantum=0
        self.__going_to_waiting_time=0
        self.__release_from_waiting_time=0
        self.__wait_time_in_waiting=0
        self.__no_of_inputs=0
        self.inputs_dictionary={}
        self.__arrival_time=arrival_time
        self.__waiting_time=0
        self.__turnaround_time=0
        self._pushed_to_ready = 0


    def set_remaining_quantum(self,quantum):
        self.__remaining_quantum=quantum

    def get_remaining_quantum(self):
        return self.__remaining_quantum

    def set_going_to_waiting_time(self,time):
        self.__going_to_waiting_time = time

    def get_going_to_waiting_time(self):
        return self.__going_to_waiting_time

    def set_releasing_time_from_waiting(self,time):
        self.__release_from_waiting_time=time

    def get_release_time_from_waiting(self):
        self.__release_from_waiting_time

    def set_wait_time_in_waiting(self,time):
        self.__wait_time_in_waiting = time

    def get_wait_time_in_waiting(self):
        return self.__wait_time_in_waiting

    def set_no_of_inputs(self,inputs):
        self.__no_of_inputs = inputs

    def get_no_of_inputs(self):
        return self.__no_of_inputs

    def set_inputs_dictionary(self,dict):
        self.__inputs_dictionary = dict

    def get_inputs_dictionary(self):
        return self.__inputs_dictionary

    def set_waiting_time(self,waiting_time):
        self.__waiting_time=waiting_time

    def set_turnaround_time(self,turnaround_time):
        self.__turnaround_time=turnaround_time

    def get_id(self):
        return self.__id

    def get_duration(self):
        return self.__duration

    def get_arrival_time(self):
        return self.__arrival_time

    def get_waiting_time(self):
        return self.__waiting_time

    def get_turnaround_time(self):
        return self.__turnaround_time

    def set_remaining_duration(self,duration):
        self.__remaining_duration=duration
    def get_remaining_duration(self):
        return self.__remaining_duration

    def display_process_info(self):
        print ('Process ID: ',self.__id)
        print ('Duration: ',self.__duration)
        print ('Arrival Time: ',self.__arrival_time)
        print ('Turnaround Time: ',self.__turnaround_time)
