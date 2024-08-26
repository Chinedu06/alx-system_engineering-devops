# Optimizes the Nginx server for handling high traffic by adjusting worker processes, connections, and other performance-related settings.

exec { 'fix-nginx-performance':
  command => "/etc/init.d/nginx stop && \
    sed -i 's/worker_connections 768;/worker_connections 4096;/g' /etc/nginx/nginx.conf && \
    sed -i 's/worker_processes auto;/worker_processes 4;/g' /etc/nginx/nginx.conf && \
    sed -i 's/keepalive_timeout 65;/keepalive_timeout 15;/g' /etc/nginx/nginx.conf && \
    sed -i 's/#tcp_nopush on;/tcp_nopush on;/g' /etc/nginx/nginx.conf && \
    sed -i 's/#tcp_nodelay on;/tcp_nodelay on;/g' /etc/nginx/nginx.conf && \
    /etc/init.d/nginx start",
  path    => '/usr/bin:/usr/sbin:/bin:/sbin',
}

