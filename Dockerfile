# Use python 3.11 base image

FROM python:3.11-slim

WORKDIR /app

# Copy requirements.txt  and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the app
CMD ["uvicorn", "app:app","--host","0.0.0.0","--port","8000"]