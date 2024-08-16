# Ensure the Apache2 package is installed
package { 'apache2':
  ensure => installed,
}

# Configure the Apache default site
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => present,
  mode    => '0644',
  source  => 'puppet:///modules/apache/000-default.conf',
  require => Package['apache2'],
}

# Restart Apache if the configuration file changes
exec { 'restart_apache':
  command     => '/etc/init.d/apache2 restart',
  refreshonly => true,
  subscribe   => File['/etc/apache2/sites-available/000-default.conf'],
}

