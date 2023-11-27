from alpine:3.18.4

COPY flag.txt /tmp/flag.txt
COPY pubkey.pem /tmp/authorized_keys


run mkdir /root/.ssh
run mv /tmp/authorized_keys /root/.ssh
run chmod 0600 /root/.ssh/authorized_keys

expose 22

entrypoint '/bin/sh'
