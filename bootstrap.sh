# install Python3.6
add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.6 -y

# update alternetives
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2

# install pip
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py

# install other dev-tools
sudo apt install -y git python-dev
sudo apt install mc -y

# install virtualenv
sudo pip install virtualenv

# Nastaveni gitu
git config --global user.name "orkasolutionscz"
git config --global user.email "fait@orkasolutions.cz"
