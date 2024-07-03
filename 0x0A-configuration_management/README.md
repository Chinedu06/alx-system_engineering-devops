# Configuration Management with Puppet

This project contains Puppet manifests for various configuration management tasks.

## Task 2: Execute a Command

The `2-execute_a_command.pp` manifest kills a process named `killmenow` using `pkill`.

### Usage

1. Install Puppet and dependencies:
    ```bash
    sudo apt-get update
    sudo apt-get install -y ruby=1:2.7+1 --allow-downgrades
    sudo apt-get install -y ruby-augeas
    sudo apt-get install -y ruby-shadow
    sudo apt-get install -y puppet
    sudo gem install puppet-lint -v 2.1.1
    ```

2. Validate the Puppet manifest:
    ```bash
    puppet-lint 2-execute_a_command.pp
    ```

3. Start the `killmenow` process (if not already running):
    ```bash
    #!/bin/bash
    while true
    do
        sleep 2
    done
    ```

    Save this script as `killmenow`, make it executable, and run it:
    ```bash
    chmod +x killmenow
    ./killmenow &
    ```

4. Apply the Puppet manifest:
    ```bash
    sudo puppet apply 2-execute_a_command.pp
    ```

5. Verify the process termination:
    ```bash
    pgrep killmenow
    ```

