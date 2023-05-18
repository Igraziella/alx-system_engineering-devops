# script to automate the debugging of Apache

file { '/var/www/html/wp-settings.php':
  ensure  => present,
  content => inline_template('<%= File.read("/var/www/html/wp-settings.php").gsub(/\.phpp/, ".php") %>'),
}
