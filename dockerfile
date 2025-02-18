# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install required dependencies
RUN pip install networkx matplotlib

# Run the script
CMD ["python", "timeline_graph.py"]