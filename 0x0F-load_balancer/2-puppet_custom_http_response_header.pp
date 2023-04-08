# automate the task of creating a custom HTTP header response, using Puppet.
package { 'nginx':
  ensure => installed,
}

file { '/etc/nginx/conf.d/custom-http-response-header.conf':
  ensure => present,
  content => 'add_header X-Served-By $hostname;',
  notify => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
