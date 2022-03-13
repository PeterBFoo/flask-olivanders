FROM python:3.9-slim
WORKDIR /
COPY . /

RUN pip install pip-tools
RUN pip-compile requirements.in
RUN pip-sync

RUN export FLASK_APP=app.py
CMD ["python3", "-m", "flask", "run", "-h", "0.0.0.0"]