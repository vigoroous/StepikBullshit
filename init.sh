sudo /etc/init.d/mysql start

# mysql -uroot -e "create database web;"
# mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"
# mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"

mysql -uroot -e "CREATE DATABASE stepic_web;"
mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"

cd /home/box/web/ask
python3 manage.py makemigrations qa
python3 manage.py migrate

sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/nginx.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo ln -sf /home/box/web/hello.py /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart
#gunicorn -b :8080 hello:app
#sudo ln -sf /home/box/web/etc/ask_conf.py /etc/gunicorn.d/ask_conf.py
#sudo gunicorn -c /etc/gunicorn.d/ask_conf.py ask.wsgi:application

cd /home/box/web/ask
gunicorn -b 0.0.0.0:8000 ask.wsgi:application