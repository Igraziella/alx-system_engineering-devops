# automate the task of creating a custom HTTP header response, using Puppet.
<<<<<<< HEAD
exec { 'command'
=======
exec { 'command':
>>>>>>> 69d8ab3d77787f2194ef82804c1dda07dfe13c4a
  command  => 'apt-get -y update;
  apt-get -y install nginx;
  sudo sed -i "/listen 80 default_server;/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-available/default;
  sudo service nginx restart',
  provider => shell,
}
