#!/bin/bash
# Set execution permissions for CGI scripts
chmod 755 /var/www/html/people.cgi
chmod 755 /var/www/html/admin.cgi
chmod 755 /var/www/html/mppl.cgi
chmod 644 /var/www/html/new.cgi
chmod 644 /var/www/html/lovers.cgi

# Set permissions for data files and directories
chmod -R 666 /var/www/html/dat/*
chmod -R 777 /var/www/html/dat
chmod -R 777 /var/www/html/user

# Start Apache in the foreground
apachectl -D FOREGROUND
