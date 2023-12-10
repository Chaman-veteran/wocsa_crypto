FROM debian:trixie-20231120-slim

COPY flag.txt /tmp/flag.txt
COPY pubkey.pem /tmp/authorized_keys

RUN useradd -m user -p user \
    ; apt-get update; apt-get install -y ssh openssh-server iproute2 \
    && echo 'PubkeyAuthentication yes' >> /etc/ssh/sshd_config \
    && mkdir -p /run/sshd \
    && mkdir -p /home/user/.ssh \
    ; mv /tmp/authorized_keys /home/user/.ssh \
    ; chmod 0600 /home/user/.ssh/authorized_keys

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 22

ENTRYPOINT '/entrypoint.sh'
