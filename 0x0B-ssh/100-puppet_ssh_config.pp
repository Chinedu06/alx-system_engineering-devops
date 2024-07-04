# 100-puppet_ssh_config.pp

# Ensure the ~/.ssh/config file exists with the correct permissions
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
}

# Ensure Host * section exists in the config file
file_line { 'Ensure Host *':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'Host *',
  match => '^Host \*',
  ensure => present,
}

# Use the private key ~/.ssh/school
file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile ',
  ensure => present,
  require => File_line['Ensure Host *'],
}

# Disable password authentication
file_line { 'Turn off passwd auth':
  path  => '/home/ubuntu/.ssh/config',
  line  => '    PasswordAuthentication no',
  match => '^\s*PasswordAuthentication ',
  ensure => present,
  require => File_line['Ensure Host *'],
}

