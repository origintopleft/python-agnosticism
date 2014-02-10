from sys import argv

if len(argv) > 1:
	import subprocess
	pass # placeholder
else:
	import sip
	sip.setapi("QString", 2)

	from PyQt4 import QtCore, QtGui, uic

	qapp = QtCore.QApplication(argv)

	cfgwindow = QtGui.QDialog()

	cfgui = uic.loadUi("config.ui", cfgwindow)

	# TODO: some bullshit about reading the config file and whatever the fuck else

	cfgwindow.show()
	sys.exit(qapp.exec_()) # maybe ???? i don't fuckin' remember man
