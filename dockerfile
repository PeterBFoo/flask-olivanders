FROM python:alpine
ENV FLASK_APP app.py
WORKDIR /
COPY . /

EXPOSE 5000

RUN pip install pip-tools
RUN pip-compile requirements.in
RUN pip-sync

CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000" ]