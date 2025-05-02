import math
import random

Q_LIMIT = 100  # Limit on queue length
BUSY = 1  # Server is busy
IDLE = 0  # Server is idle

# Global variables
next_event_type = 0
num_custs_delayed = 0
num_delays_required = 0
num_events = 2
num_in_q = 0
server_status = IDLE

area_num_in_q = 0.0
area_server_status = 0.0
mean_interarrival = 0.0
mean_service = 0.0
sim_time = 0.0
time_last_event = 0.0
total_of_delays = 0.0
time_arrival = [0.0] * (Q_LIMIT + 1)
time_next_event = [0.0, 0.0, 1.0e+30]  # Events: 1 (arrival), 2 (departure)

def initialize():
    global sim_time, server_status, num_in_q, time_last_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status, time_next_event
    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    time_next_event[1] = sim_time + expon(mean_interarrival)
    time_next_event[2] = 1.0e+30

def timing():
    global sim_time, next_event_type
    min_time_next_event = float('inf')
    next_event_type = 0
    
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i
    
    if next_event_type == 0:
        outfile.write(f"\nEvent list empty at time {sim_time}\n")
        exit(1)
    
    sim_time = min_time_next_event

def arrive():
    global num_in_q, server_status, num_custs_delayed, total_of_delays, time_next_event
    
    time_next_event[1] = sim_time + expon(mean_interarrival)
    
    if server_status == BUSY:
        num_in_q += 1
        if num_in_q > Q_LIMIT:
            outfile.write(f"\nOverflow of the queue at time {sim_time}\n")
            exit(2)
        time_arrival[num_in_q] = sim_time
    else:
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        server_status = BUSY
        time_next_event[2] = sim_time + expon(mean_service)

def depart():
    global num_in_q, server_status, num_custs_delayed, total_of_delays, time_next_event
    
    if num_in_q == 0:
        server_status = IDLE
        time_next_event[2] = 1.0e+30
    else:
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        time_next_event[2] = sim_time + expon(mean_service)
        for i in range(1, num_in_q):
            time_arrival[i] = time_arrival[i + 1]
        num_in_q -= 1
    
def report():
    output_buffer = []
    output_buffer.append("\nSingle-server queueing system\n")
    output_buffer.append(f"\nAverage delay in queue: {total_of_delays / num_custs_delayed:.3f} minutes\n")
    output_buffer.append(f"Average number in queue: {area_num_in_q / sim_time:.3f}\n")
    output_buffer.append(f"Server utilization: {area_server_status / sim_time:.3f}\n")
    output_buffer.append(f"Time simulation ended: {sim_time:.3f} minutes\n")

    outfile.write("".join(output_buffer))  # Efficient single write


def update_time_avg_stats():
    global area_num_in_q, area_server_status, time_last_event
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event

def expon(mean):
    return -mean * math.log(random.random())

def main():
    global mean_interarrival, mean_service, num_delays_required, outfile, num_events
    
    # Read input parameters
    with open("./mm1.in", "r") as infile:
        mean_interarrival, mean_service, num_delays_required = map(float, infile.readline().split())
        num_delays_required = int(num_delays_required)

    outfile = open("mm1.out", "w")
    
    outfile.write("Single-server queueing system\n\n")
    outfile.write(f"Mean interarrival time{mean_interarrival:11.3f} minutes\n\n")
    outfile.write(f"Mean service time{mean_service:16.3f} minutes\n\n")
    outfile.write(f"Number of customers{num_delays_required:14d}\n\n")
    
    
    # Initialize the simulation
    num_events = 2
    initialize()
    
    while num_custs_delayed < num_delays_required:
        timing()
        update_time_avg_stats()
        
        if next_event_type == 1:
            arrive()
        elif next_event_type == 2:
            depart()
    
    # Generate the report
    report()
    
    outfile.close()

if __name__ == "__main__":
    main()
