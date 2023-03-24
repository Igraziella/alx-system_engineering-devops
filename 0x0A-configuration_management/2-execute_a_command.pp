# Creates a manifest that kills the process named killmenow
exec { 'kills a process named killmenow':
  command  => 'pkill killnenow',
  path     => '/bin:/usr/bin',
  provider => 'shell',
}
