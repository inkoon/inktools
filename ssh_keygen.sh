NAME=$1
USER=$2
HOST=$3

ssh-keygen -f ~/.ssh/id_rsa_$NAME
ssh-copy-id -i ~/.ssh/id_rsa_$NAME.pub $USER@$HOST
