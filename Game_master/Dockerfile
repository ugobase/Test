FROM python:3.9-slim
WORKDIR /master-app
COPY ./requirements.txt /master-app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . /master-app
EXPOSE 5002
CMD ["python", "game_master.py"]

