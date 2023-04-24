FROM python:latest
WORKDIR /app
COPY consume3.py .
copy requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt
# Expose port 5000
EXPOSE 3306
# RUN pip install json
# RUN python3 rope.py

CMD ["python", "consume3.py"]

