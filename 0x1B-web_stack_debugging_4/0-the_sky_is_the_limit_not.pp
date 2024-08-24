# This Puppet manifest is intended to optimize the Nginx server for handling high traffic by adjusting worker processes and connections.

exec { 'fix-nginx-performance':
  command => "/etc/init.d/nginx stop && \
    sed -i 's/worker_connections 768;/worker_connections 4096;/g' /etc/nginx/nginx.conf && \
    sed -i 's/worker_processes auto;/worker_processes 4;/g' /etc/nginx/nginx.conf && \
    /etc/init.d/nginx start",
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}

