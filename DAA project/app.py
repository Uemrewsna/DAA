from flask import Flask, render_template, request, jsonify
from scheduling import GreedyScheduler, PriorityScheduler, DynamicLoadBalancer, JobSimulator, PerformanceAnalyzer
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    # Get data from the form
    strategy = request.form.get('strategy')
    num_resources = int(request.form.get('num_resources', 0))  # Default to 0 if not provided
    num_jobs = 10  # Example, could be dynamic or user-defined

    if strategy == "1":
        scheduler = GreedyScheduler(num_resources)
    elif strategy == "2":
        scheduler = PriorityScheduler()
    elif strategy == "3":
        scheduler = DynamicLoadBalancer(num_resources)
    else:
        return jsonify({"error": "Invalid strategy"})

    # Simulate job arrival
    simulator = JobSimulator(num_jobs=num_jobs, max_duration=10)
    jobs = simulator.generate_jobs()

    results = []
    resources_distribution = []  # List to store resource assignment for each job
    for job in jobs:
        if strategy == "1":
            resource = scheduler.schedule_job(job)
            results.append(f"Assigned job {job} to resource {resource}")
            resources_distribution.append(resource)  # Collect data for graph
        elif strategy == "2":
            priority = random.randint(1, 10)
            scheduler.add_job(job, priority)
        elif strategy == "3":
            resource, loads = scheduler.assign_job(job)
            results.append(f"Assigned job {job} to resource {resource}")
            resources_distribution.append(resource)  # Collect data for graph

    # Show performance metrics
    analyzer = PerformanceAnalyzer()
    # Assuming some performance metrics collection happens here

    # Send results and distribution data back to the frontend
    return jsonify({"results": results, "distribution": resources_distribution})

if __name__ == "__main__":
    app.run(debug=True)


'''import random
from flask import Flask, render_template, request, jsonify
from scheduling import GreedyScheduler, PriorityScheduler, DynamicLoadBalancer, JobSimulator, PerformanceAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    strategy = request.form.get('strategy')
    num_resources = int(request.form.get('num_resources', 0))
    num_jobs = 10

    if strategy == "1":
        scheduler = GreedyScheduler(num_resources)
    elif strategy == "2":
        scheduler = PriorityScheduler()
    elif strategy == "3":
        scheduler = DynamicLoadBalancer(num_resources)
    else:
        return jsonify({"error": "Invalid strategy"})

    simulator = JobSimulator(num_jobs=num_jobs, max_duration=10)
    jobs = simulator.generate_jobs()

    results = []
    steps = []
    chart_data = [0] * num_resources  # Initialize chart data

    for job in jobs:
        if strategy == "1":
            resource = scheduler.schedule_job(job)
            results.append(f"Assigned job {job} to resource {resource}")
            chart_data[resource] += 1  # Update chart data
            steps.append(f"Job {job} assigned to resource {resource}.")
        elif strategy == "2":
            priority = random.randint(1, 10)
            scheduler.add_job(job, priority)
            steps.append(f"Job {job} added with priority {priority}.")
        elif strategy == "3":
            resource, loads = scheduler.assign_job(job)
            results.append(f"Assigned job {job} to resource {resource} - Current load: {loads}")
            steps.append(f"Job {job} assigned to resource {resource}. Loads: {loads}")

    analyzer = PerformanceAnalyzer()

    return jsonify({
        "results": results,
        "steps": steps,
        "labels": [f'Resource {i}' for i in range(num_resources)],
        "chartData": chart_data
    })

if __name__ == "__main__":
    app.run(debug=True)
'''