# 100-puppet_ssh_config.pp
# This Puppet manifest ensures the SSH client configuration is set to use the private key ~/.ssh/school
# and disables password authentication in the /etc/ssh/ssh_config file.

file_line { 'Ensure Host *':
  path  => '/etc/ssh/ssh_config',
  line  => 'Host *',
  match => '^Host \*',
  ensure => present,
}

file_line { 'Declare identity file':
  path  => '/etc/ssh/ssh_config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile ',
  ensure => present,
  require => File_line['Ensure Host *'],
}

file_line { 'Turn off password auth':
  path  => '/etc/ssh/ssh_config',
  line  => '    PasswordAuthentication no',
  match => '^\s*PasswordAuthentication ',
  ensure => present,
  require => File_line['Ensure Host *'],
}

