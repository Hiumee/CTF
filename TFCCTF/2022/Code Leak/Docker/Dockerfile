FROM python:3.10

RUN /usr/sbin/useradd --no-create-home -u 1000 ctf

WORKDIR /home/ctf

COPY main.py .
COPY controller.py .

RUN apt-get update
RUN apt-get install -y socat

RUN chown -R root:root /home/ctf

USER ctf

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"python3 main.py"
