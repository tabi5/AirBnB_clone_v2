# Configures a web server for deployment of web_static.

#  variable to store the Nginx configuration
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

# Install Nginx package
package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

# New variable to store the directory paths
$data_dir = '/data'
$web_static_dir = "${data_dir}/web_static"
$releases_dir = "${web_static_dir}/releases"
$test_dir = "${releases_dir}/test"
$shared_dir = "${web_static_dir}/shared"

# Create necessary directories
file { $data_dir:
  ensure  => 'directory'
} ->

file { $web_static_dir:
  ensure => 'directory'
} ->

file { $releases_dir:
  ensure => 'directory'
} ->

file { $test_dir:
  ensure => 'directory'
} ->

file { $shared_dir:
  ensure => 'directory'
} ->

# New variable to store the index.html file path
$index_file = "${test_dir}/index.html"

# Create index.html file for testing
file { $index_file:
  ensure  => 'present',
  content => "Holberton School Puppet\n"
} ->

# New variable to store the symbolic link path
$current_link = "${web_static_dir}/current"

# Create symbolic link to the current release
file { $current_link:
  ensure => 'link',
  target => $test_dir
} ->

# Set ownership and permissions
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

#  variable to store the Nginx directories
$www_dir = '/var/www'
$html_dir = "${www_dir}/html"

# Create necessary directories for Nginx
file { $www_dir:
  ensure => 'directory'
} ->

file { $html_dir:
  ensure => 'directory'
} ->

#  variable to store the Nginx files
$nginx_index_file = "${html_dir}/index.html"
$nginx_404_file = "${html_dir}/404.html"

# Create index.html and 404.html files for Nginx
file { $nginx_index_file:
  ensure  => 'present',
  content => "Holberton School Nginx\n"
} ->

file { $nginx_404_file:
  ensure  => 'present',
  content => "Ceci n'est pas une page\n"
} ->

#  variable to store the Nginx default site path
$default_site_path = '/etc/nginx/sites-available/default'

# Configure Nginx default site
file { $default_site_path:
  ensure  => 'present',
  content => $nginx_conf
} ->

# Restart Nginx service
exec { 'nginx restart':
  path => '/etc/init.d/'
}
