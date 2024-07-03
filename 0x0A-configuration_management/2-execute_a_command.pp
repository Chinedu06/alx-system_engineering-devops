# This Puppet manifest kills a process named killmenow using pkill
exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/usr/bin/pgrep killmenow',
}

