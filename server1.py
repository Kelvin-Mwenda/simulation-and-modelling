import math
import random

# Constants for queue simulation
Q_LIMIT = 100  # Maximum allowed length of the queue
BUSY = 1  # Server status: serving a customer
IDLE = 0  # Server status: no customer being served

# Global variables to track simulation state
next_event_type = 0  # Type of the next event to be processed
num_custs_delayed = 0  # Total number of customers that have been delayed
num_delays_required = 0  # Target number of customers to process
num_events = 2  # Number of event types (arrival and departure)
num_in_q = 0  # Current number of customers in the queue
server_status = IDLE  # Current status of the server

# Statistical tracking variables
area_num_in_q = 0.0  # Area under the queue length curve (for average calculation)
area_server_status = (
    0.0  # Area under the server status curve (for utilization calculation)
)
mean_interarrival = 0.0  # Mean time between customer arrivals
mean_service = 0.0  # Mean service time
sim_time = 0.0  # Current simulation time
time_last_event = 0.0  # Time of the last event processed
total_of_delays = 0.0  # Total delay experienced by all customers

# Array to store arrival times of customers in the queue
time_arrival = [0.0] * (Q_LIMIT + 1)

# Array to track the time of next events
# Index 1: Next arrival time
# Index 2: Next departure time
time_next_event = [0.0, 0.0, 1.0e30]


def initialize():
    """
    Initialize the simulation parameters and set up the first arrival event.
    Resets all statistical and state tracking variables.
    """
    global sim_time, server_status, num_in_q, time_last_event, num_custs_delayed, total_of_delays, area_num_in_q, area_server_status, time_next_event
    sim_time = 0.0
    server_status = IDLE
    num_in_q = 0
    time_last_event = 0.0
    num_custs_delayed = 0
    total_of_delays = 0.0
    area_num_in_q = 0.0
    area_server_status = 0.0
    # Schedule the first arrival event
    time_next_event[1] = sim_time + expon(mean_interarrival)
    # Set departure event to infinity until first customer arrives
    time_next_event[2] = 1.0e30


def timing():
    """
    Determine the type and time of the next event to be processed.
    Finds the minimum time from the event list.
    """
    global sim_time, next_event_type
    min_time_next_event = float("inf")
    next_event_type = 0

    # Find the event with the earliest occurrence
    for i in range(1, num_events + 1):
        if time_next_event[i] < min_time_next_event:
            min_time_next_event = time_next_event[i]
            next_event_type = i

    # Error handling if no events are found
    if next_event_type == 0:
        outfile.write(f"\nEvent list empty at time {sim_time}\n")
        exit(1)

    # Update simulation time to the time of the next event
    sim_time = min_time_next_event


def arrive():
    """
    Handle customer arrival event.
    If server is busy, customer joins the queue.
    If server is idle, customer is served immediately.
    """
    global num_in_q, server_status, num_custs_delayed, total_of_delays, time_next_event

    # Schedule next arrival
    time_next_event[1] = sim_time + expon(mean_interarrival)

    if server_status == BUSY:
        # Server is busy, customer joins the queue
        num_in_q += 1
        # Check for queue overflow
        if num_in_q > Q_LIMIT:
            outfile.write(f"\nOverflow of the queue at time {sim_time}\n")
            exit(2)
        # Record arrival time of this customer
        time_arrival[num_in_q] = sim_time
    else:
        # Server is idle, customer is served immediately
        delay = 0.0
        total_of_delays += delay
        num_custs_delayed += 1
        # Mark server as busy
        server_status = BUSY
        # Schedule departure event
        time_next_event[2] = sim_time + expon(mean_service)


def depart():
    """
    Handle customer departure event.
    If queue is empty, server becomes idle.
    Otherwise, next customer in queue starts being served.
    """
    global num_in_q, server_status, num_custs_delayed, total_of_delays, time_next_event

    if num_in_q == 0:
        # No customers waiting, server becomes idle
        server_status = IDLE
        time_next_event[2] = 1.0e30
    else:
        # Serve next customer from the queue
        delay = sim_time - time_arrival[1]
        total_of_delays += delay
        num_custs_delayed += 1
        # Schedule departure for this customer
        time_next_event[2] = sim_time + expon(mean_service)
        # Shift arrival times in queue
        for i in range(1, num_in_q):
            time_arrival[i] = time_arrival[i + 1]
        num_in_q -= 1


def report():
    """
    Generate a report with key simulation statistics.
    Calculates and writes average delay, queue length, server utilization, etc.
    """
    output_buffer = []
    output_buffer.append("\nSingle-server queueing system\n")
    output_buffer.append(
        f"\nAverage delay in queue: {total_of_delays / num_custs_delayed:.3f} minutes\n"
    )
    output_buffer.append(f"Average number in queue: {area_num_in_q / sim_time:.3f}\n")
    output_buffer.append(f"Server utilization: {area_server_status / sim_time:.3f}\n")
    output_buffer.append(f"Time simulation ended: {sim_time:.3f} minutes\n")

    outfile.write("".join(output_buffer))  # Efficient single write


def update_time_avg_stats():
    """
    Update time-averaged statistical variables.
    Calculates areas under the queue length and server status curves.
    """
    global area_num_in_q, area_server_status, time_last_event
    # Calculate time since last event
    time_since_last_event = sim_time - time_last_event
    time_last_event = sim_time
    # Update areas for statistical calculations
    area_num_in_q += num_in_q * time_since_last_event
    area_server_status += server_status * time_since_last_event


def expon(mean):
    """
    Generate exponential random variate.
    Used for generating inter-arrival and service times.
    """
    return -mean * math.log(random.random())


def main():
    """
    Main simulation routine.
    Reads input parameters, initializes simulation,
    runs simulation loop, and generates final report.
    """
    global mean_interarrival, mean_service, num_delays_required, outfile, num_events

    # Read input parameters from file
    with open("./mm1.in", "r") as infile:
        mean_interarrival, mean_service, num_delays_required = map(
            float, infile.readline().split()
        )
        num_delays_required = int(num_delays_required)

    # Open output file for writing simulation results
    outfile = open("mm1.out", "w")

    # Write input parameters to output file
    outfile.write("Single-server queueing system\n\n")
    outfile.write(f"Mean interarrival time{mean_interarrival:11.3f} minutes\n\n")
    outfile.write(f"Mean service time{mean_service:16.3f} minutes\n\n")
    outfile.write(f"Number of customers{num_delays_required:14d}\n\n")

    # Initialize the simulation
    num_events = 2
    initialize()

    # Main simulation loop
    while num_custs_delayed < num_delays_required:
        timing()  # Determine next event
        update_time_avg_stats()  # Update statistical trackers

        # Process the event
        if next_event_type == 1:
            arrive()  # Customer arrival event
        elif next_event_type == 2:
            depart()  # Customer departure event

    # Generate final simulation report
    report()

    # Close output file
    outfile.close()


if __name__ == "__main__":
    main()
