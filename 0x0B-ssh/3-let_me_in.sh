#!/usr/bin/env bash
# This script adds a given SSH public key to the authorized_keys file for the ubuntu user

# Ensure we are the ubuntu user
if [ "$(whoami)" != "ubuntu" ]; then
  echo "This script must be run as the ubuntu user."
  exit 1
fi

# Create .ssh directory if it doesn't exist
mkdir -p ~/.ssh

# Add the SSH public key to the authorized_keys file
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN' >> ~/.ssh/authorized_keys

# Set the correct permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys

# Restart the SSH daemon to apply changes
sudo systemctl restart ssh

