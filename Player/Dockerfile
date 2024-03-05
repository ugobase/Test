FROM python:3.9-slim
WORKDIR /player-app
COPY ./requirements.txt /player-app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /player-app
EXPOSE 5000
CMD ["python", "server.py"]