#!/bin/bash
#gksu INSTALLERS/install_pkg_core.sh
#gksu INSTALLERS/install_pkg_mysql.sh
#gksu INSTALLERS/install_psp.sh
chmod +x INSTALLERS/*.sh
gksu python python/wbrc.py $HOME