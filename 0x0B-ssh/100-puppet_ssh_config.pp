# Configure server to authenticate only through ssh keys
include stdlib

file_line { 'Turn off password auth':
	ensure => 'present',
	path => '/etc/ssh/ssh_config',
	line => 'PasswordAuthentication no',
	match => '^PasswordAuthentication'
}

file_line { 'Declare identity file':
	ensure => 'present',
	path =>'/etc/ssh/ssh_config',
	line => 'IdentityFile ~/.ssh/school',
	match => '^IdentityFile'
}
