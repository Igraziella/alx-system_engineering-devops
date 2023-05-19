# A puppet manifest to change user limit

exec { 'change_value_to_40':
  command => "/bin/sed -i 's/5/40/g' /etc/security/limits.conf",
}

exec { 'change_value_to_30':
  command => "/bin/sed -i 's/4/30/g' /etc/security/limits.conf",
}
