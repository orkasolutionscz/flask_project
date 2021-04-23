apt update && apt upgrade -y
# install Python3.6
# add-apt-repository ppa:deadsnakes/ppa
# apt update
# apt install python3.8

# update alternetives
#update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
# update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 2

# install pip
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

# install other dev-tools
apt install -y git python-dev
apt install mc -y

# install virtualenv
sudo pip install virtualenv