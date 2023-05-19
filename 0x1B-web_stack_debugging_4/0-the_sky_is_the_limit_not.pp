# A puppet manifest to change user limit

exec { 'increase_ulimit':
  command => 'sed -i "s/15/2046/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Restart Nginx
exec { 'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
