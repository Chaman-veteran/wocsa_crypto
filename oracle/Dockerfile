FROM python:3.9-slim-buster

COPY docker_ed25519.pub /tmp/authorized_keys


RUN apt-get update -y; \
    apt-get install -y lib32z1 xinetd ssh openssh-server iproute2 && \
    pip3 install pycryptodome && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo 'PubkeyAuthentication yes' >> /etc/ssh/sshd_config \
    && mkdir /root/.ssh \
    ; mv /tmp/authorized_keys /root/.ssh \
    ; chmod 0600 /root/.ssh/authorized_keys

RUN useradd -m user && \
    chown -R root:root /home/user

COPY app /home/user/
COPY xinetd /etc/xinetd.d/user

COPY entrypoint.sh /tmp/entrypoint.sh
run chmod +x /tmp/entrypoint.sh

WORKDIR /home/user

EXPOSE 9999
EXPOSE 22

entrypoint "/tmp/entrypoint.sh"