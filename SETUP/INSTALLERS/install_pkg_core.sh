export DEBIAN_FRONTEND=noninteractive;

rm /var/lib/dpkg/lock;
rm /var/lib/apt/lists/lock;
killall -9 apt-get;
killall -9 dpkg;

export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.old/*.deb >> Log

dpkg -i INSTALLERS/debs/apt.mysql/lib*.deb >> Log
dpkg -i INSTALLERS/debs/apt.mysql/mysql-server*.deb >> Log
dpkg -i INSTALLERS/debs/apt.mysql/mysql-client*.deb >> Log
dpkg -i INSTALLERS/debs/apt.mysql/mysql-common*.deb >> Log
dpkg -i INSTALLERS/debs/apt.mysql/python*.deb >> Log

dpkg -i INSTALLERS/debs/apt.google/*.deb >> Log
dpkg -i INSTALLERS/debs/google*.deb >> Log

cp INSTALLERS/debs/apache2.conf /etc/apache/apache2.conf
echo "Apache hopefully reconfigured" >> Log
/etc/init.d/apache2 restart >> Log

