import matplotlib.pyplot as plt
import datetime
import os

# Log file setup
LOG_FILE = "timeline.log"

def log_message(message):
    """Print and save log messages."""
    print(message)
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")

# Function to safely get user input
def get_input(prompt, validation_func=None):
    """Get user input with optional validation."""
    while True:
        try:
            user_input = input(prompt).strip()
            if validation_func:
                validation_func(user_input)
            log_message(f"User input received: {user_input}")
            return user_input
        except ValueError as e:
            log_message(f"ERROR: {e}")
            print(f"Invalid input: {e}. Please try again.")

# Validation functions
def validate_year(year_str):
    """Ensure the input is a valid year."""
    if not year_str.isdigit():
        raise ValueError("Year must be a number.")
    year = int(year_str)
    if year < 1900 or year > datetime.datetime.now().year + 10:
        raise ValueError(f"Year out of range (1900-{datetime.datetime.now().year + 10}).")

def validate_date(date_str):
    """Ensure the input is a valid YYYY-MM format or 'present'."""
    if date_str.lower() == "present":
        return
    try:
        datetime.datetime.strptime(date_str, "%Y-%m")
    except ValueError:
        raise ValueError("Date must be in YYYY-MM format or 'present'.")

# Get timeline range
log_message("Starting timeline creation process...")
start_year = int(get_input("Enter starting year of the timeline (e.g., 2015): ", validate_year))
end_year = int(get_input("Enter ending year of the timeline (e.g., 2024): ", validate_year))

# Get number of jobs
num_jobs = int(get_input("Enter the number of jobs: ", lambda x: int(x) if x.isdigit() and int(x) > 0 else ValueError("Must be a positive number.")))

jobs = []
for i in range(num_jobs):
    print(f"\nJob {i+1}:")
    job_title = get_input("Enter job title: ")
    start_date = get_input("Enter job start date (YYYY-MM): ", validate_date)
    end_date = get_input("Enter job end date (YYYY-MM or 'present'): ", validate_date)
    jobs.append((job_title, start_date, end_date))

# Convert dates into numerical values for plotting
def parse_date(date_str):
    """Convert date string to numerical representation."""
    if date_str.lower() == "present":
        return datetime.datetime.now().year + datetime.datetime.now().month / 12.0
    return datetime.datetime.strptime(date_str, "%Y-%m").year + datetime.datetime.strptime(date_str, "%Y-%m").month / 12.0

log_message("Generating timeline graph...")

# Create the figure
fig, ax = plt.subplots(figsize=(12, 5))

# Draw main timeline
ax.plot([start_year, end_year], [0, 0], color="black", linewidth=2)
log_message("Main timeline drawn.")

# Draw job timelines
y_offset = 1  # Start offset for job placement
for job_title, start, end in jobs:
    start_x = parse_date(start)
    end_x = parse_date(end)
    
    ax.plot([start_x, end_x], [y_offset, y_offset], label=job_title, linewidth=4)
    ax.text(start_x, y_offset + 0.2, job_title, fontsize=10, ha="left", va="center")
    log_message(f"Job '{job_title}' added from {start} to {end}.")
    y_offset += 1  # Move the next job to a different row to avoid overlap

# Formatting the graph
ax.set_yticks([])
ax.set_xticks(range(start_year, end_year + 1))
ax.set_xlabel("Year")
ax.set_title("Job Timeline")

plt.legend()
plt.grid(axis="x", linestyle="--", alpha=0.6)

# Ensure output directory exists
output_dir = "output"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the figure as a JPG
output_filename = os.path.join(output_dir, "timeline.jpg")
plt.savefig(output_filename, dpi=300)

log_message(f"Timeline graph saved as {output_filename}")

plt.show()