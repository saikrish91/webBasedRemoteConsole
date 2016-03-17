export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/lib*.deb

export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/mysql-server*.deb

export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/mysql-server_5.1.61-0ubuntu0.11.10.1_all.deb

export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/mysql-server-5.1_5.1.61-0ubuntu0.11.10.1_i386

export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/mysql-server-core-5.1_5.1.61-0ubuntu0.11.10.1_i386
echo "Correcting mysql dependencies" >> Log


export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/mysql-server-core-5.1_5.1.61-0ubuntu0.11.10.1_i386

export DEBIAN_FRONTEND=noninteractive;
dpkg --configure -a >> Log
echo "dpkg corrections" >> Log

export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/mysql-cl*.deb

export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/mysql-co*.deb


export DEBIAN_FRONTEND=noninteractive;
dpkg -i INSTALLERS/debs/apt.mysql/python*.deb


export DEBIAN_FRONTEND=noninteractive;
mysqladmin -u root password root
echo "MySQL password hopefully reset" >> Log
