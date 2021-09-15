sudo /etc/init.d/mysql start

# mysql -uroot -e "create database web;"

# mysql -uroot -e "create user 'box'@'localhost' identified by '1234';"

# mysql -uroot -e "grant all privileges on stepic_web.* to 'box'@'localhost' with grant option;"

mysql -uroot -e "CREATE DATABASE stepic_web;"

mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"

cd /home/box/web/ask

python3 manage.py makemigrations qa

python3 manage.py migrate