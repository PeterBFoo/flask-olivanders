FROM python:alpine
ENV FLASK_APP app.py

RUN mkdir ollivanders
WORKDIR /ollivanders
COPY . /ollivanders/

EXPOSE 5000

RUN pip install pip-tools
RUN pip-compile requirements.in
RUN pip-sync
RUN pip uninstall pip-tools

CMD [ "python", "app.py" ]