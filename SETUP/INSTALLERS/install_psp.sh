rm -rf /var/www/index.html
cp INSTALLERS/debs/index.html /var/www/index.html
cp INSTALLERS/debs/apache2.conf /etc/apache2/apache2.conf
echo "Apache hopefully reconfigured" >> Log
/etc/init.d/apache2 restart >> Log

mkdir /tmp/wbrc/
cp INSTALLERS/modules.zip /tmp/wbrc/
unzip /tmp/wbrc/modules.zip -d /tmp/wbrc/
rm -rf /var/www/modules
rm -rf /var/www/ver6.2
cp -R /tmp/wbrc/modules /var/www/
cp -R /tmp/wbrc/ver6.2 /var/www/
rm /usr/share/pixmaps/wbrc.png
cp INSTALLERS/wbrc.png /usr/share/pixmaps/
chmod 777 /usr/share/pixmaps/wbrc.png
cp INSTALLERS/wbrc.desktop $@/Desktop/
chmod 777 $@/Desktop/wbrc.desktop
/etc/init.d/apache2 restart

export DEBIAN_FRONTEND=noninteractive;
mysqladmin -u root password root;
echo "MySQL password hopefully reset" >> Log;