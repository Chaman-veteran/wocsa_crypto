FROM python:3.9-slim-buster

COPY docker_ed25519.pub /tmp/authorized_keys


RUN apt-get update -y; \
    apt-get install -y lib32z1 xinetd iproute2 && \
    pip3 install pycryptodome && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m user && \
    chown -R root:root /home/user

COPY app /home/user/
COPY xinetd /etc/xinetd.d/user

COPY entrypoint.sh /tmp/entrypoint.sh
run chmod +x /tmp/entrypoint.sh

WORKDIR /home/user

EXPOSE 9999

entrypoint "/tmp/entrypoint.sh"