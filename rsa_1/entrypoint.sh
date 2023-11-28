#!/bin/sh
ssh-keygen -A
exec /usr/sbin/sshd -D -e "$@" &
exec /bin/sh