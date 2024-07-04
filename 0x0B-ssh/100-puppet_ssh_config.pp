# 100-puppet_ssh_config.pp
# This Puppet manifest ensures the SSH client configuration is set to use the private key ~/.ssh/school
# and disables password authentication.

file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
}

file_line { 'Ensure Host *':
  path  => '/home/ubuntu/.ssh/config',
  line  => 'Host *',
  match => '^Host \*',
  ensure => present,
}

file_line { 'Declare identity file':
  path  => '/home/ubuntu/.ssh/config',
  line  => '    IdentityFile ~/.ssh/school',
  match => '^\s*IdentityFile ',
  ensure => present,
  require => File_line['Ensure Host *'],
}

file_line { 'Turn off password auth':
  path  => '/home/ubuntu/.ssh/config',
  line  => '    PasswordAuthentication no',
  match => '^\s*PasswordAuthentication ',
  ensure => present,
  require => File_line['Ensure Host *'],
}

