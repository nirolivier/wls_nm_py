#	======================================================
#	This script stops, deploys and starts an application
#	to a managed server.
#	
#	Author: 	Razafindrabekoto Nirina Olivier
#	Date:		08/05/2016
#	Version:	1.0
#	========================================================

import socket
import os
import string
import const
import credentialConst
import time as time_
import threading




#	Starts the managed server
#	@param servername: the name of the server to start
#	@param types: can take the following value: 'Server' or 'Cluster'
def startMgServer(servername,types,url):
	# if the server is stopped then run the server
	print "Starting the managed server " + servername + " with type "+types+" by connection to server instance "+url
	print "..."
	if not url and url is not None:
		start(servername, types, url, block='false')		
	else:
		start(servername, types, block='false')

	print '[OK] : Server ' +servername+' is started successfully.'


#	Starts the application
#	@param servername: the name of the server to start
#	@param appName: the name of the application to start
def stop_app(servername, appName):
	progress = stopApplication(appName, targets=servername)
	if progress.isCompleted():
		print 'Application ' +appName +' is successfully stopped.'
	elif progress.isRunning():
		print 'Application ' +appName +' is running.'
	else:
		print 'Unable to stop the application ' +appName
		progress.printStatus()
		exit()
	progress.printStatus()


#	check if the application is active
#	@param servername: the name of the server
#	@param appName: the name of the application to start
def is_app_active(servername, appName):
	return check_app_state(servername, appName,"STATE_ACTIVE")

#	check if the application is failed
#	@param servername: the name of the server
#	@param appName: the name of the application to start
def is_app_failed(servername, appName):
	return check_app_state(servername, appName,"STATE_FAILED")

#	check if the application is new
#	@param servername: the name of the server
#	@param appName: the name of the application to start
def is_app_failed(servername, appName):
	return check_app_state(servername, appName,"STATE_NEW")

#	check if the application state
#   @param servername: the name of the server
#	@param appName: the name of the application to start
def check_app_state(servername, appName,appstate):
	domainRuntime()
	cd('/AppRuntimeStateRuntime/AppRuntimeStateRuntime')
	currentstate = cmo.getCurrentState(appName, servername)
	print 'The current state of application ' + appName + ' is ' + currentstate
	print 'The expected state of application ' + appName + ' is ' + appstate
	
	if appstate == currentstate:
		return true
	
	serverConfig()
	return false

#	Stops the managed server
#	@param entityType: can take the following value: 'Server' or 'Cluster'
#	@param servername: the name of the server to start
def stopMgServer(servername,entityType):
	# if the server is running then stops the server
	print ''
	print 'Stopping the server ' + servername
	print '...'
	print ''

	if is_running(servername):
		shutdown(servername, entityType, ignoreSessions='false', timeOut=0, block='false')
		print '[OK]	: Server '+servername+' is successfully stopped.'
	else:
		print '[OK]	: Server '+servername+' is already stopped.'
	

#	check if the managed server is starting
#	@param servername: the name of the server to start
def is_starting(servername):
	return hasState(servername,"STARTING")

#	check if the managed server is started
#	@param servername: the name of the server to start
def is_stopped(servername):
	return hasState(servername,"SHUTDOWN")

#	Check if the managed server is running
#	@param servername: the name of the server to start
def is_running(servername):
	return hasState(servername,"RUNNING")

#	Check if the server is in given state
#	@param servername the name of the server
#	@param state a server state
def hasState(servername,state):
	flag = false
	serverConfig()
	servers = cmo.getServers()
	domainRuntime()
	for server in servers:
		if server.getName() == servername:
			cd('/ServerLifeCycleRuntimes/'+servername)
			serverState = cmo.getState()
			if serverState == state:
				flag=true
				break

	serverConfig()
	return flag

def is_available(address,port):
	flag = false
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		res=s.connect_ex((address, int(port)))
		if res == 0:
			flag = true
			print 'The port '+str(port)+ ' is already used on address '+ address
		else:
			flag = false
			print 'The port '+str(port)+ ' is not used on address '+ address
		s.close()
	except:
		print '[ERROR] Cannot detect if port '+str(port)+ ' is available on address '+address
	
	return flag


#	Deploy an application to a managed server
#	deploy('myApp', '/opt/devtools/server/weblogic/user_project/deploy', targets='myServer',timeout=0)
#	@param appName: the name of the deployed application
#	@param appPath: the path of the application to deploy
def deployApp(appName, path,servername):
	print ''
	print 'Deploying the application ' + appName + ' from '+path
	print ''
	print '....'	

	progress = deploy(appName, path, targets=servername,timeout=0)
	if progress.isCompleted():	
		print '[OK]	: Application '+appName+' is successfully deployed.'
		progress.printStatus()
	elif progress.isFailed():
		print '[ERROR]	: Application '+appName+' is unsuccessfully deployed.'
		print '[ERROR]	message : '+progress.getMessage()
		print '[ERROR]	status 	: '+progress.printStatus()
	

#	Check if the given application was currently deployed
#	@param appName the name of the deployed application
def isDeployed(appName):
	apps = cmo.getAppDeployments()
	for app in apps:
		if app.getName() == appName:
			print 'The application ' + appName + ' is deployed.'
			return true
	print 'No application with name ' + appName + ' is deployed.'
	return false

#	Undeploy an application to a managed server
#	@param appName: the name of the application to undeploy
#	@param servername: the name of the server
def undeployApp(appName,servername):
	print ''
	print 'Undeploying the application ' + appName
	print ''
	print '....'

	if isDeployed(appName):
		if is_app_active(servername,appName):
			stop(servername,appName)

		progress = undeploy(appName,targets=servername,timeout=0)
		if progress.isCompleted():
			print '[OK]	: Application '+appName+' is successfully undeployed'
			progress.printStatus()
		elif progress.isFailed():
			print '[ERROR]	: Application '+appName+' is unsuccessfully undeployed.'
			print '[ERROR]	message : '+progress.getMessage()
			print '[ERROR]	status 	: '+progress.printStatus()
			exit()
		

def connectNM():
	# connect to the current node manager
	# nmConnect('weblogic', 'webl0gic', host='localhost', port='5556', domainName='test_dom', domainDir='/opt/devtools/server/weblogic/user_project/domains/test_dom', nmType='plain',verbose='false')
	nmConnect(credentialConst.USER_NAME, credentialConst.PASSWORD, const.NM_HOST, const.NM_PORT, const.APP_DOMAIN_NAME, const.APP_DOMAIN_DIR, const.NM_TYPE)

def startNM():
	# start node manager
	# startNodeManager(verbose='true', NodeManagerHome='/opt/devtools/server/weblogic/provider/wls1036_dev/wlserver/common/nodemanager', ListenPort='5556', ListenAddress='localhost')
	startNodeManager(verbose='true', NodeManagerHome=const.NM_HOME, ListenPort=const.NM_PORT, ListenAddress=const.NM_HOST)
	#connectNM()

def startAdminServer():
	# Error: java.rmi.NoSuchObjectException: The object identified by: '31' could not be found.  Either it was has not been exported or it has been collected by the distributed garbage collector.
	# Solve: remove ADMIN_URL props
	# nmStart('AdminServer',domainDir='/opt/devtools/server/weblogic/user_project/domains/test_dom')
	prps = makePropertiesObject("Username="+credentialConst.USER_NAME+";Password="+credentialConst.PASSWORD+";weblogic.ListenPort="+str(const.WLS_ADMIN_PORT))
	if not is_available(const.WLS_ADMIN_HOST,const.WLS_ADMIN_PORT):
		connectNM()
		nmStart(const.WLS_ADMIN_SERVER_NAME,domainDir=const.APP_DOMAIN_DIR,props=prps)
		nmDisconnect()
		

def connectAdminServer():
	# connect('weblogic', 'webl0gic','t3://localhost:7001')
	connect(credentialConst.USER_NAME, credentialConst.PASSWORD,const.WLS_ADMIN_T3_URL)

def currentMilliSecond():
	return long(round(time_.time() * 1000))  


#	Program entry point.
if __name__ == "main":
	print ''
	print '======================================================================'
	print 'Starting the application deployment into the following managed server'
	print 'managed server name :' + const.APP_SERVER_NAME
	print 'application name :' + const.APP_NAME
	print '======================================================================'
	print ''
	
	redirect(const.APP_DEPLOY_LOG)

	# try connect to running node manager
	try:
		connectNM()
	 	nmDisconnect()
	except:
		print 'Node Manager is not running. Starting Node Manager and retrying to connect...'
		startNM()
		

	# try connect to weblogic server
	try:
		connectAdminServer()
	except:
		print 'Unable to connect to AdminServer, server not running. Please see '+ const.APP_DEPLOY_LOG +' for complete error'
		startAdminServer()
		connectAdminServer()
		
	if isDeployed(const.APP_NAME) and is_app_active(const.APP_SERVER_NAME,const.APP_NAME):
		stop_app(const.APP_SERVER_NAME,const.APP_NAME)

	overtime = 30000l
	timeinit = currentMilliSecond()
	while not check_app_state(const.APP_SERVER_NAME,const.APP_NAME,"STATE_NEW"):
		if overtime < (currentMilliSecond() - timeinit):
			print 'Timeout while switching to the state STATE_NEW after the application '+const.APP_NAME+' was stopped.'
			exit()

	stopMgServer(const.APP_SERVER_NAME,const.TYPE_SERVER)
	undeployApp(const.APP_NAME,const.APP_SERVER_NAME)
	deployApp(const.APP_NAME,const.APP_DEPLOY_PATH_FROM,const.APP_SERVER_NAME)
	
	startMgServer(const.APP_SERVER_NAME,const.TYPE_SERVER,const.WLS_ADMIN_T3_URL)

	print ''
	print '======================================================================'
	print 'End of application deployment'
	print '======================================================================'
	print ''

