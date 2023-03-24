# Installing flask version 2.1.0 on a puppet agent.
package { 'flask':
  ensure   => '2.1.0',
  provider => pip3,
}
