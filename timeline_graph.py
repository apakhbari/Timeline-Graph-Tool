import matplotlib.pyplot as plt
import datetime

# Function to get user input
def get_input(prompt):
    print(prompt, end="", flush=True)
    return input()

# Get timeline range
start_year = int(get_input("Enter starting year of the timeline (e.g., 2015): "))
end_year = int(get_input("Enter ending year of the timeline (e.g., 2024): "))

# Get number of jobs
num_jobs = int(get_input("Enter the number of jobs: "))

jobs = []
for i in range(num_jobs):
    print(f"\nJob {i+1}:")
    job_title = get_input("Enter job title: ")
    start_date = get_input("Enter job start date (YYYY-MM): ")
    end_date = get_input("Enter job end date (YYYY-MM): ")
    jobs.append((job_title, start_date, end_date))

# Convert dates into numerical values for plotting
def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m").year + datetime.datetime.strptime(date_str, "%Y-%m").month / 12.0

fig, ax = plt.subplots(figsize=(12, 5))

# Draw main timeline
ax.plot([start_year, end_year], [0, 0], color="black", linewidth=2)

# Draw job timelines
y_offset = 1  # Start offset for job placement
for job_title, start, end in jobs:
    start_x = parse_date(start)
    end_x = parse_date(end)
    
    ax.plot([start_x, end_x], [y_offset, y_offset], label=job_title, linewidth=4)
    ax.text(start_x, y_offset + 0.2, job_title, fontsize=10, ha="left", va="center")
    y_offset += 1  # Move the next job to a different row to avoid overlap

# Formatting the graph
ax.set_yticks([])
ax.set_xticks(range(start_year, end_year + 1))
ax.set_xlabel("Year")
ax.set_title("Job Timeline")

plt.legend()
plt.grid(axis="x", linestyle="--", alpha=0.6)

# Save the figure as a JPG
output_filename = "timeline.jpg"
plt.savefig(output_filename, dpi=300)
print(f"\nTimeline graph saved as {output_filename}")

plt.show()