# Creates a manifest that kills the process named killmenow
exec { 'killmenow':
  command => 'pkill killmenow',
  path    => '/bin:/usr/bin',
  onlyif  => 'pgrep killmenow',
}
