# this puppet manifest configures a web server to serve a static page
exec { 'apt-get update':
  command => '/bin/apt-get update'
}

package { 'nginx':
  ensure => 'installed',
}

exec { 'create directory1':
  command => '/bin/mkdir -p /data/web_static/releases/test/',
}

exec { 'create directory2':
  command => '/bin/mkdir -p /data/web_static/shared/',
}

exec { 'create index.html':
  command => '/bin/echo "<html>
  <head>
  </head>
  <body>
    Hello World!
  </body>
</html>" > /data/web_static/releases/test/index.html',
}

exec { 'remove_web_static_current':
  command => '/bin/rm -rf /data/web_static/current',
  onlyif  => '/bin/test -L /data/web_static/current',
}

exec { 'create symlink':
  command => '/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
}

exec { 'change ownership':
  command => '/bin/chown -R ubuntu:ubuntu /data/',
}

exec { 'update nginx config':
  command => '/bin/sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default',
}

exec { 'restart nginx':
  command => '/sbin/service nginx restart',
}
