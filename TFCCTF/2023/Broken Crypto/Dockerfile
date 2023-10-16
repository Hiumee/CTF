FROM node:latest

RUN /usr/sbin/useradd --no-create-home -u 1001 ctf

WORKDIR /home/ctf

COPY main.js .

RUN apt-get update
RUN apt-get install -y socat

RUN chown -R root:root /home/ctf

RUN npm install prompt-sync

USER ctf

EXPOSE 1337

CMD socat TCP-LISTEN:1337,reuseaddr,fork EXEC:"node main.js"
