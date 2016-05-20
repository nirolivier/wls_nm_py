#	======================================================
#	This script stops a managed server.
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
	print 'Stopping the following server'
	print 'Server name :' + const.APP_SERVER_NAME
	print '======================================================================'
	print ''
	
	prepareConnection()
	stopMgServer(const.APP_SERVER_NAME,const.TYPE_SERVER)
	
	print ''
	print '======================================================================'
	print 'Server '+const.APP_SERVER_NAME+' is successfully stopped.'
	print '======================================================================'
	print ''

