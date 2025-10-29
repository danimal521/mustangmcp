# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file first for efficient caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .
RUN ls

# Expose the port your FastMCP server runs on (adjust if needed)
EXPOSE 8000

# Command to run FastMCP server
#CMD ["python", "-m", "fastmcp", "serve", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["fastmcp", "serve", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["python", "-m", "fastmcp.server"]
CMD ["python", "app.py"]