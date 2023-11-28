from alpine:3.18.4

copy flag.txt /tmp/flag.txt
copy pubkey.pem /tmp/authorized_keys

run apk update; apk add --no-cache openssh \
    && echo 'PubkeyAuthentication yes' >> /etc/ssh/sshd_config \
    && mkdir /root/.ssh \
    ; mv /tmp/authorized_keys /root/.ssh \
    ; chmod 0600 /root/.ssh/authorized_keys

expose 22

copy entrypoint.sh /
run chmod +x /entrypoint.sh

entrypoint '/entrypoint.sh'
