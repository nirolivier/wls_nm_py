#	======================================================
#	This script stops, deploys and starts an application
#	to a managed server.
#	
#	Author: 	Razafindrabekoto Nirina Olivier
#	Date:		08/05/2016
#	Version:	1.0
#	========================================================

import string
import const

execfile('core.py')


#	Program entry point.
if __name__ == "main":
	print ''
	print '======================================================================'
	print 'Starting the application deployment into the following managed server'
	print 'managed server name :' + const.APP_SERVER_NAME
	print 'application name :' + const.APP_NAME
	print '======================================================================'
	print ''
	
	prepareConnection()
	stopMgServer(const.APP_SERVER_NAME,const.TYPE_SERVER)
	undeployApp(const.APP_NAME,const.APP_SERVER_NAME)
	deployApp(const.APP_NAME,const.APP_DEPLOY_PATH_FROM,const.APP_SERVER_NAME)	
	startMgServer(const.APP_SERVER_NAME,const.TYPE_SERVER,const.WLS_ADMIN_T3_URL)

	print ''
	print '======================================================================'
	print 'End of application deployment'
	print '======================================================================'
	print ''

