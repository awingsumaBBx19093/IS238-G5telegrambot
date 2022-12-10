#!/bin/bash

if [[ -z "$2" ]]; then
    echo "Must provide path to pem file and the remote server (e.g. 'security.pem' ec-user@amazon.com)" 1>&2
    exit 1
fi
if [[ -z "$1" ]]; then
    echo "Must provide path to pem file" 1>&2
    exit 1
fi
if [[ -z "$2" ]]; then
    echo "Must provide the remote server (e.g. ec-user@amazon.com)" 1>&2
    exit 1
fi

ssh -i $1 $2 "rm -r ~/app; mkdir -p ~/app"
scp -i $1 -r ${PWD}/Dockerfile $2:~/app/
scp -i $1 -r ${PWD}/requirements.txt $2:~/app/
scp -i $1 -r ${PWD}/src $2:~/app/
ssh -i $1 $2 "
  docker build -t g5-telegrambot ~/app/.
  docker run --rm -d g5-telegrambot
"