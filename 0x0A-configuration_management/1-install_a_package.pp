# Installing flask version 2.1.0 on a puppet agent.
exec { 'puppet-lint':
  command => '/usr/bin/apt-get -y install puppet-lint -v 2.1.0',
}
