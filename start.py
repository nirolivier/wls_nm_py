#	======================================================
#	This script starts a server.
#	
#	Author: 	Razafindrabekoto Nirina Olivier
#	Date:		08/05/2016
#	Version:	1.0
#	========================================================

import string
import const

execfile('./core.py')

#	Program entry point.
if __name__ == "main":
	print ''
	print '======================================================================'
	print 'Starting the following server'
	print 'Server name :' + const.APP_SERVER_NAME
	print '======================================================================'
	print ''
	
	prepareConnection()
	stopMgServer(const.APP_SERVER_NAME,const.TYPE_SERVER)
	startMgServer(const.APP_SERVER_NAME,const.TYPE_SERVER,const.WLS_ADMIN_T3_URL)
	
	print ''
	print '======================================================================'
	print 'Server '+ const.APP_SERVER_NAME + 'is successfully started.'
	print '======================================================================'
	print ''

