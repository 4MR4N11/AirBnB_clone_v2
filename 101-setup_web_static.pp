# this puppet manifest configures a web server to serve a static page
class web_server_setup {

  package { 'update':
    ensure => 'latest',
  }

  package { 'nginx':
    ensure => 'installed',
  }

  file { [
    '/data/web_static/releases/test',
    '/data/web_static/shared',
  ]:
    ensure => 'directory',
  }

  file { '/data/web_static/releases/test/index.html':
    content => '<html>
  <head>
  </head>
  <body>
    Hello World!
  </body>
</html>',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
  }

  file { '/data/web_static/current':
    ensure  => 'absent',
    require => File['/data/web_static/releases/test/index.html'],
  }

  file { '/data/web_static/current':
    ensure  => 'link',
    target  => '/data/web_static/releases/test',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file_line { 'configure_nginx':
    path    => '/etc/nginx/sites-available/default',
    line    => 'location /hbnb_static/ { alias /data/web_static/current/; }',
    match   => '^ *listen 80 default_server;',
    ensure  => present,
    require => Package['nginx'],
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure     => 'running',
    enable     => true,
    subscribe  => File_line['configure_nginx'],
  }
}

include web_server_setup
