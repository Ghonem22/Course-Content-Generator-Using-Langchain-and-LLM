# 
FROM python:3.9

# 
WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# 
COPY ./app /app/code

#
WORKDIR /app/code

#
#CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT}"]

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "main:app"]
