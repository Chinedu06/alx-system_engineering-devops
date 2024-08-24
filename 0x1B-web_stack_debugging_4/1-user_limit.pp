# This Puppet manifest adjusts the file descriptor limits to prevent 'Too many open files' errors and reload the Nginx configuration.

file { '/etc/security/limits.conf':
  ensure  => file,
  content => "holberton soft nofile 4096\nholberton hard nofile 8192\n",
  notify  => Exec['restart_nginx'],
}

exec { 'restart_nginx':
  command     => '/usr/sbin/nginx -s reload',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}

