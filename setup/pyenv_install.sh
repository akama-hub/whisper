#!/bin/bash

sudo apt update
sudo apt upgrade -y

git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
source ~/.bash_profile

# pyenv install --list

sudo apt install build-essential libbz2-dev libreadline-dev \
libsqlite3-dev libffi-dev curl libncursesw5-dev \
libdb-dev xz-utils libxml2-dev libxmlsec1-dev \
libffi-dev libgdbm-dev liblzma-dev \
libssl-dev tk-dev uuid-dev zlib1g-dev

pyenv install 3.8

pyenv global 3.8