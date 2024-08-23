#!/usr/bin/env bash
set -eou pipefail

sudo apt-get update
sudo apt-get install -y gpg sudo wget curl python3-venv python3 python3-dev build-essential clang libclang-dev

sudo install -dm 755 /etc/apt/keyrings

wget -qO - http://download.sgjp.pl/apt/sgjp.gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/morfeusz-archive-keyring.gpg 1> /dev/null
wget -qO - https://mise.jdx.dev/gpg-key.pub | gpg --dearmor | sudo tee /etc/apt/keyrings/mise-archive-keyring.gpg 1> /dev/null

echo "deb [signed-by=/etc/apt/keyrings/morfeusz-archive-keyring.gpg arch=amd64] http://download.sgjp.pl/apt/ubuntu noble main" | sudo tee /etc/apt/sources.list.d/morfeusz.list
echo "deb [signed-by=/etc/apt/keyrings/mise-archive-keyring.gpg arch=amd64] https://mise.jdx.dev/deb stable main" | sudo tee /etc/apt/sources.list.d/mise.list

sudo apt update
sudo apt-get install -y morfeusz2-dictionary-polimorf morfeusz2-dictionary-sgjp libmorfeusz2 libmorfeusz2-dev mise

# curl https://mise.run | sh

