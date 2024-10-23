

import random
 
# Define the scheduling algorithms

class GreedyScheduler:
    def __init__(self, num_resources):
        self.num_resources = num_resources
        self.resources = [0] * num_resources  # Initialize resource loads

    def schedule_job(self, job):
        # Logic for greedy scheduling (simplified example)
        resource_index = self.resources.index(min(self.resources))
        self.resources[resource_index] += job  # Assume job is a duration
        return resource_index

class PriorityScheduler:
    def __init__(self):
        self.job_queue = []

    def add_job(self, job, priority):
        self.job_queue.append((job, priority))
        self.job_queue.sort(key=lambda x: x[1])  # Sort by priority

    def schedule_jobs(self):
        return [job for job, _ in self.job_queue]  # Return jobs in order of priority

class DynamicLoadBalancer:
    def __init__(self, num_resources):
        self.num_resources = num_resources
        self.resources = [0] * num_resources

    def assign_job(self, job):
        resource_index = self.resources.index(min(self.resources))
        self.resources[resource_index] += job
        return resource_index, self.resources

class JobSimulator:
    def __init__(self, num_jobs, max_duration):
        self.num_jobs = num_jobs
        self.max_duration = max_duration

    def generate_jobs(self):
        return [random.randint(1, self.max_duration) for _ in range(self.num_jobs)]

class PerformanceAnalyzer:
    def print_metrics(self):
        # Logic to analyze and print performance metrics
        print("Performance metrics displayed.")

# Main function to run the scheduling logic
def main():
    # Choose scheduler type
    print("Choose scheduling strategy:")
    print("1. Greedy Scheduling")
    print("2. Priority-Based Scheduling")
    print("3. Dynamic Load Balancing")
    strategy = int(input())

    if strategy == 1:
        num_resources = int(input("Enter number of resources: "))
        scheduler = GreedyScheduler(num_resources)
    elif strategy == 2:
        scheduler = PriorityScheduler()
    elif strategy == 3:
        num_resources = int(input("Enter number of resources: "))
        scheduler = DynamicLoadBalancer(num_resources)
    else:
        print("Invalid option")
        return

    # Simulate job arrival
    simulator = JobSimulator(num_jobs=10, max_duration=10)
    jobs = simulator.generate_jobs()

    # Analyze performance
    analyzer = PerformanceAnalyzer()

    for job in jobs:
        if strategy == 1:
            resource = scheduler.schedule_job(job)
            print(f"Assigned job {job} to resource {resource}")
        elif strategy == 2:
            priority = random.randint(1, 10)
            scheduler.add_job(job, priority)
        elif strategy == 3:
            resource, loads = scheduler.assign_job(job)
            print(f"Assigned job {job} to resource {resource}")
            print(f"Current load distribution: {loads}")

    if strategy == 2:
        print("Scheduled jobs by priority:")
        print(scheduler.schedule_jobs())

    # Show performance
    analyzer.print_metrics()

if __name__ == "__main__":
    main()
