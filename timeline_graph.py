import networkx as nx
import matplotlib.pyplot as plt
import datetime

def get_user_input():
    """Get user input for jobs dynamically."""
    start_year = int(input("Enter starting year of the timeline (e.g., 2015): "))
    end_year = int(input("Enter ending year of the timeline (e.g., 2024): "))

    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))

    for i in range(num_jobs):
        job_name = input(f"Enter name of job {i + 1}: ")
        start_date = input(f"Enter start date (YYYY-MM) of {job_name}: ")
        end_date = input(f"Enter end date (YYYY-MM) of {job_name} (or 'present' if ongoing): ")

        jobs.append({
            "name": job_name,
            "start": start_date,
            "end": end_date if end_date.lower() != "present" else f"{end_year}-12",
        })

    return start_year, end_year, jobs

def generate_timeline_graph(start_year, end_year, jobs):
    """Generate a flat, non-colliding timeline graph."""
    G = nx.DiGraph()

    # Main timeline nodes
    years = list(range(start_year, end_year + 1))
    for i in range(len(years) - 1):
        G.add_edge(years[i], years[i + 1])

    # Job edges
    job_positions = {}  # Track vertical positions to avoid overlap
    job_offset = 1  # Space out job edges

    for job in jobs:
        start_year, start_month = map(int, job["start"].split("-"))
        end_year, end_month = map(int, job["end"].split("-"))

        job_start = f"{start_year}-{start_month:02d}"
        job_end = f"{end_year}-{end_month:02d}"

        job_level = len(job_positions)  # Assign a unique level to prevent collisions
        job_positions[job["name"]] = job_level

        G.add_edge(job_start, job_end, label=job["name"])

    return G, job_positions

def draw_timeline(G, job_positions):
    """Draw the timeline graph."""
    pos = nx.spring_layout(G, seed=42, k=0.3)  # Adjust layout for clarity

    plt.figure(figsize=(12, 6))

    # Draw main timeline
    edges = [(u, v) for u, v in G.edges if "-" not in str(u)]
    nx.draw_networkx_nodes(G, pos, nodelist=G.nodes, node_color="lightblue", node_size=800)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="black", width=2)

    # Draw job edges
    for job, level in job_positions.items():
        edges = [(u, v) for u, v, d in G.edges(data=True) if "label" in d and d["label"] == job]
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color="red", width=2, style="dashed")

    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    plt.title("Job Timeline Graph", fontsize=14)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    start_year, end_year, jobs = get_user_input()
    G, job_positions = generate_timeline_graph(start_year, end_year, jobs)
    draw_timeline(G, job_positions)
