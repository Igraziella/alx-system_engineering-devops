#!/usr/bin/puppet
# setting up my client's config file using puppet
include stdlib

file_line { 'turn off password':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
}

file_line { 'identity file':
  ensure  => present,
  line    => 'IdentityFile ~/.ssh/school',
  path    => '/etc/ssh/ssh_config',
}
