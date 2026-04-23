#!/bin/bash
echo "===== USER CREATION SCRIPT ====="
echo "Enter new username:"
read username
sudo adduser $username
sudo usermod -aG sudo $username
echo "===== USER $username CREATED SUCCESSFULLY ====="
groups $username
