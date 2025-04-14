FROM erfannoorani/deepcoder-base:latest
WORKDIR /app
RUN apt-get update && apt-get install -y git
COPY handler.py .
COPY requirements.txt .  # If you have one
RUN pip install --no-cache-dir -r requirements.txt  # If requirements.txt exists
CMD ["python", "-u", "handler.py"]
