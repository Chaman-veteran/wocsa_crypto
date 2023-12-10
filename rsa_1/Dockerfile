FROM debian:trixie-20231120-slim

COPY flag.txt /tmp/flag.txt
COPY key.pub /tmp/authorized_keys

RUN apt-get update; apt-get install -y ssh openssh-server iproute2 \
    && echo 'PubkeyAuthentication yes' >> /etc/ssh/sshd_config \
    && echo 'AuthorizedKeysFile %h/.ssh/authorized_keys' >> /etc/ssh/sshd_config \
    && echo 'PasswordAuthentication no' >> /etc/ssh/sshd_config \
    && mkdir -p /run/sshd \
    && mkdir -p /root/.ssh \
    && mv /tmp/authorized_keys /root/.ssh \
    ; chmod 0600 /root/.ssh/authorized_keys

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 22

WORKDIR /root

ENTRYPOINT '/entrypoint.sh'
