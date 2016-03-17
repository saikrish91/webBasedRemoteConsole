import gtk
import commands
import sys

def ui_imageset(filename,w,h):
	im=gtk.Image()
	pixbuf=gtk.gdk.pixbuf_new_from_file(filename)
	scaled_buf=pixbuf.scale_simple(w,h,gtk.gdk.INTERP_BILINEAR)
	im.set_from_pixbuf(scaled_buf)
	return im

def arch_chk():
	arch=commands.getstatusoutput("uname -m")[1]
	if arch in ('i386','i486','i586','i686'):
		return True
	else:
		return False

def btnWinMySQLclk(self,win):
	"""Backup mysql data next"""
	win.set_visible(False)
	winMySQLDB()

def btn1clk(self):
	""""""
	#win1.set_visible(False)
	btn1.set_visible(False)
	winMode()

def btnModeclk(self,o2,w):
	""""""
	w.set_visible(False)
	if o2.state==1:
		winConfirmOnline()
	else:
		winOffline()

def btnCO2clk(self,w3):
	""""""
	w3.set_visible(False)
	winOnline()

def btnCO1clk(self,w3):
	""""""
	w3.set_visible(False)
	winOffline()

def btnOnlineclk(self,win,statlabel):
	""""""
	
	statlabel.set_label("Installing main packages.")
	commands.getstatusoutput("export DEBIAN_FRONTEND=noninteractive;INSTALLERS/install_pkg_apt.sh")
	statlabel.set_label("Installed main packages.")
	
	statlabel.set_label("Running post PSP installing scripts.")
	commands.getstatusoutput("INSTALLERS/install_psp.sh "+sys.argv[1])
	statlabel.set_label("Python Server Pages installed.")
	
	if arch_chk():
		statlabel.set_label("Installing Google Chrome browser.")
		commands.getstatusoutput("dpkg -i INSTALLERS/debs/google*.deb")
		statlabel.set_label("Installed Google Chrome browser.")
	else:
		commands.getstatusoutput("dpkg -i INSTALLERS/debs64/google*.deb")
	
	win.set_visible(False)
	winMySQL()
	"""btnOnlineclick Function terminates"""

def btnOfflineclk(self,win,statlabel):
	""""""
	statlabel.set_label("Installing CORE packages.")
	commands.getstatusoutput("INSTALLERS/install_pkg_core.sh")
	statlabel.set_label("Core packages were installed.")
	
	statlabel.set_label("Installing MySQL packages.")
	commands.getstatusoutput("INSTALLERS/install_pkg_mysql.sh")
	statlabel.set_label("MySQL packages installed.")
	
	statlabel.set_label("Installing Python Server Pages.")
	commands.getstatusoutput("INSTALLERS/install_psp.sh "+sys.argv[1])
	statlabel.set_label("Python Server Pages installed.")
	
	statlabel.set_label("Installing Google Chrome browser.")
	commands.getstatusoutput("dpkg -i INSTALLERS/debs/google*.deb")
	statlabel.set_label("Installed Google Chrome browser.")
	
	win.set_visible(False)
	winMySQL()


def winMode():
	winMode=gtk.Window()
	print "winMode"
	winMode.set_title("Choose your mode..")
	winMode.resize(500,300)
	vMode=gtk.VBox()
	winMode.show_all()
	print "Displayed"
	labelMode=gtk.Label("Please wait...")
	vMode.pack_start(labelMode)
	winMode.show_all()
	if arch_chk():
		conn=commands.getstatusoutput("ping -c 1 ubuntu.com")[0]
		print "Pinged"
		print conn
		o1Mode=gtk.RadioButton(label="I wish to use the offline packages distributed by WBRC")
		o2Mode=gtk.RadioButton(group=o1Mode,label="I wish to use the internet (stable, recommended)")
		if conn==0:
			labelMode.set_label("Please choose your mode of installation.\nAn internet connection was detected in your system.")
			vMode.pack_start(o1Mode)
			vMode.pack_start(o2Mode)
		else:
			labelMode.set_label("No internet was detected in your system.\nWBRC offline packages will now install.")
		winMode.show_all()
		btnMode=gtk.Button("Next")
		hMode=gtk.HButtonBox()
		hMode.pack_end(btnMode)
		vMode.pack_end(hMode)
		winMode.add(vMode)
		winMode.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		winMode.connect("delete-event", gtk.main_quit)
		btnMode.connect("clicked",btnModeclk,o2Mode,winMode)
		winMode.show_all()
	else:
		winMode.set_visible(False)
		winOnline()



def winConfirmOnline():
	win3=gtk.Window()
	win3.set_title("Online Setup")
	win3.resize(500,300)
	v3=gtk.VBox()
	h4=gtk.HBox()
	img_clock=ui_imageset("python/clock_red.png",120,120)
	h4.pack_start(img_clock)
	label3=gtk.Label("Please note that using the internet requires at least 72MB of data to download and it can take time. If you wish to still continue, press Next. \nIf you wish to use the offline WBRC packages instead, press Offline.\nEnsure that you close all package managers such as Synaptic before proceeding.")
	h4.pack_end(label3)
	btn4=gtk.Button("Offline")
	btn3=gtk.Button("Next")
	h3=gtk.HButtonBox()
	h3.pack_start(btn4)
	h3.pack_end(btn3)
	v3.pack_start(h4)
	v3.pack_end(h3)
	win3.add(v3)
	win3.set_position(gtk.WIN_POS_CENTER_ALWAYS)
	win3.connect("delete-event", gtk.main_quit)
	btn4.connect("clicked",btnCO1clk,win3)
	btn3.connect("clicked",btnCO2clk,win3)
	win3.show_all()

def winOnline():
	msg=""
	internet=True
	if not arch_chk():
		msg="Not a 32 bit system, resorting to online installation.\n"
	conn=commands.getstatusoutput("ping -c 1 ubuntu.com")[0]
	if conn !=0:
		internet=False
	win5=gtk.Window()
	win5.set_title("Please wait..")
	win5.resize(500,300)
	win5.set_position(gtk.WIN_POS_CENTER_ALWAYS)
	v5=gtk.VBox()
	h6=gtk.HBox()
	if internet:
		label5=gtk.Label(msg+"Please press Install.")
		label7=gtk.Label("Note that this process takes several minutes depending\non your internet connection speed. Total download:72MB.\nDSL 2Mbps+ : 10mins\nDSL 512kbps : 30mins\nDialup : 1.5hrs")
		img_clock=ui_imageset("python/clock_red.png",120,120)
		h6.pack_start(img_clock)
		h6.pack_end(label7)
		label6=gtk.Label("")
		v5.pack_start(label5)
		v5.pack_start(h6)
		v5.pack_start(label6)
		btn5=gtk.Button("Install")
		h5=gtk.HButtonBox()
		h5.pack_end(btn5)
		v5.pack_end(h5)
		win5.add(v5)
		win5.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		win5.connect("delete-event", gtk.main_quit)
		btn5.connect("clicked",btnOnlineclk,win5,label6)
		win5.show_all()
		label6.set_label("")
	else:
		label5=gtk.Label(msg+"Please note that internet is required to complete the installation.\nRun the wizard again when you have an active internet connection.")
		v5.pack_start(label5)
		btn5=gtk.Button("Abort")
		v5.pack_end(btn5)
		btn5.connect("clicked",gtk.main_quit)
		win5.add(v5)
		win5.set_position(gtk.WIN_POS_CENTER_ALWAYS)
		win5.connect("delete-event", gtk.main_quit)
		win5.show_all()

def winOffline():
	""""""
	win5=gtk.Window()
	win5.set_title("Please wait..")
	win5.resize(500,300)
	v5=gtk.VBox()
	h6=gtk.HBox()
	label5=gtk.Label("Press Install to begin with offline installation.")
	label7=gtk.Label("Note that the installation may take a few minutes\n(upto 10 minutes). DO NOT close the installation wizard.")
	img_clock=ui_imageset("python/clock_red.png",120,120)
	h6.pack_start(img_clock)
	h6.pack_end(label7)
	label6=gtk.Label("")
	v5.pack_start(label5)
	v5.pack_start(h6)
	v5.pack_start(label6)
	btn5=gtk.Button("Install")
	h5=gtk.HButtonBox()
	h5.pack_end(btn5)
	v5.pack_end(h5)
	win5.add(v5)
	win5.set_position(gtk.WIN_POS_CENTER_ALWAYS)
	win5.connect("delete-event", gtk.main_quit)
	btn5.connect("clicked",btnOfflineclk,win5,label6)
	win5.show_all()

def mysql_check():
	try:
		import MySQLdb as mysql
		conn=mysql.connect(user='root',passwd='root')
		return True
	except:
		return False

def mysql_check_button(self,label,button,h,v,img_mysql1,img_sql,btnAbort):
	a=mysql_check()
	if a==True:
		label.set_label("MySQL is properly installed and set in your system.\nPress Next to continue.")
		v.remove(img_mysql1)
		v.remove(img_sql)
		h.remove(btnAbort)
		h.pack_end(button)
		h.show_all()
	else:
		v.pack_start(img_mysql1)
		h.pack_start(btnAbort)
		label.set_label("Try again to setup MySQL, or press Abort to stop the installation.\nFollow the command based instruction as well before aborting installation.")
		h.show_all()
		v.show_all()

def myInitDB():
	import MySQLdb as mysql
	conn=mysql.connect(user='root',passwd='root')
	c=conn.cursor()
	try:
		c.execute("DROP DATABASE wbrc")
	except:
		pass
	c.execute("CREATE DATABASE wbrc")
	commands.getstatusoutput("mysql -u root wbrc < python/wbrc6.2.sql --password='root'")

def winMySQLDB():
	""""""
	winSQL=gtk.Window()
	winSQL.set_title("Initializing website")
	winSQL.resize(500,300)
	winSQL.set_position(gtk.WIN_POS_CENTER_ALWAYS)
	label1=gtk.Label("Websites entries have been initialized. Press Next to continue.")
	v=gtk.VBox()
	v.pack_start(label1)
	winSQL.add(v)
	btn=gtk.Button("Next")
	v.pack_start(btn)
	myInitDB()
	winSQL.show_all()
	btn.connect("clicked",btnSQLDB,winSQL)

def btnSQLDB(self,winSQL):
	""""""
	winSQL.set_visible(False)
	winRoot=gtk.Window()
	winRoot.set_title("System Credentials")
	winRoot.resize(500,300)
	label1=gtk.Label("Enter this computer's root password:")
	e1=gtk.Entry()
	e1.set_visibility(False)
	label2=gtk.Label("Re-enter this computer's root password:")
	e2=gtk.Entry()
	e2.set_visibility(False)
	h1=gtk.HBox()
	h1.pack_start(label1)
	h1.pack_start(e1)
	h2=gtk.HBox()
	h2.pack_start(label2)
	h2.pack_start(e2)
	btn=gtk.Button("Next")
	label3=gtk.Label("If you haven't set up your root password yet, do it before completing this installation.\nEnter the following command in a terminal:\nsudo passwd root")
	img_root=ui_imageset("python/root_pwd.png",406,151)
	v=gtk.VBox()
	v.pack_start(h1)
	v.pack_start(h2)
	v.pack_start(label3)
	v.pack_start(img_root)
	v.pack_start(btn)
	winRoot.add(v)
	winRoot.set_position(gtk.WIN_POS_CENTER_ALWAYS)
	btn.connect("clicked",btnRoot,winRoot,e1,e2,label3)
	winRoot.show_all()


def btnRoot(self,win,e1,e2,lbl):
	if e1.get_text() != "":
		if e1.get_text()==e2.get_text():
			setRoot(e1.get_text(),win)
	else:
		lbl.set_text("Enter valid root password")
		win.show_all()

def setRoot(pwd,win):
	import MySQLdb as mysql
	conn=mysql.connect(user='root',passwd='root',db="wbrc")
	c=conn.cursor()
	c.execute("UPDATE HOSTS SET HPWD='"+pwd+"' WHERE HOSTID=1")
	winLast(win)

def winLast(win):
	win.set_visible(False)
	win1.set_title("Installation complete!")
	label1.set_label("Use google-chrome for optimum performance. \nPress Finish to complete the installation.")
	btn2=gtk.Button("Finish")
	h1.remove(btn1)
	h1.pack_end(btn2)
	btn2.connect("clicked", gtk.main_quit)
	h1.show_all()
	clk_icn=ui_imageset("python/click_icon.png",100,64)
	lblicn=gtk.Label("Double click the icon on your Desktop to launch\npsthe Web Based Remote Console.")
	v1.pack_end(clk_icn)
	v1.pack_end(lblicn)
	v1.show_all()

def winMySQL():
	""""""
	img_sql1=ui_imageset("python/mysql_pwd.png",384,177)
	img_sql=ui_imageset("python/mysql_server.png",450,300)
	win5=gtk.Window()
	win5.set_title("Testing MySQL connectivity")
	win5.resize(500,300)
	mc=mysql_check()
	v=gtk.VBox()
	img_clock=ui_imageset("python/clock_red.png",120,120)
	label1=gtk.Label("Status message")
	v.pack_start(label1)
	h2=gtk.HBox()
	h3=gtk.HBox()
	lbl1=gtk.Label("Enter your computer's root password:")
	lbl2=gtk.Label("Re-enter your computer's root password:")
	t1=gtk.Entry
	btn=gtk.Button("Next")
	btn1=gtk.Button("Refresh")
	h=gtk.HButtonBox()
	h.pack_end(btn1)
	h.pack_end(btn)
	v.pack_end(h)
	win5.add(v)
	if mc:
		label1.set_label("MySQL is properly installed and set in your system.\nPress Next to continue.")
	else:
		label1.set_label("MySQL has not been setup properly.\nInstall MySQL from Software Package Manager as illustrated below.\nEnsure that you provide 'root' as the root password (without the quotes).\nThen press the refresh button to refresh.\n")
		h.remove(btn)
		v.pack_start(img_sql)
	win5.set_position(gtk.WIN_POS_CENTER_ALWAYS)
	btnAbort=gtk.Button("Abort")
	btnAbort.connect("clicked", gtk.main_quit)
	win5.connect("delete-event", gtk.main_quit)
	btn1.connect("clicked",mysql_check_button,label1,btn,h,v,img_sql1,img_sql,btnAbort)
	btn.connect("clicked",btnWinMySQLclk,win5)
	win5.show_all()

win1=gtk.Window()
win1.set_title("Setup")
win1.resize(400,200)
v1=gtk.VBox()
label1=gtk.Label("Welcome to the Web Based Remote Console setup wizard.\nFollow the instructions in the next few screens to install the software.\n\nNOTE:Close all package managers such as Synaptic before proceeding.")
v1.pack_start(label1)
btn1=gtk.Button("Next")
h1=gtk.HButtonBox()
h1.pack_end(btn1)
v1.pack_end(h1)
win1.add(v1)
win1.set_position(gtk.WIN_POS_CENTER_ALWAYS)
win1.connect("delete-event", gtk.main_quit)
btn1c=btn1.connect("clicked",btn1clk)
win1.show_all()

gtk.main()
