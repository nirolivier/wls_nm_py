APP_NAME='myApp'
APP_DEPLOY_PATH_FROM='/opt/devtools/server/weblogic/user_project/deploy/myApp.war'
APP_SERVER_NAME='myServer'
APP_DOMAIN_NAME='test_dom'
APP_DOMAIN_DIR='/opt/devtools/server/weblogic/user_project/domains/test_dom'
APP_DEPLOY_LOG='/opt/devtools/server/weblogic/provider/wls1036_dev/logs/deploy.log'

NM_HOST='localhost'
NM_PORT='5556'
# If you specify plain for nmType, you must manually set the SecureListener parameter in nodemanager.properties to false. 
# Otherwise, the nmConnect command will fail.
NM_TYPE='plain'
NM_HOME='/opt/devtools/server/weblogic/provider/wls1036_dev/wlserver/common/nodemanager'

TYPE_SERVER='Server'
TYPE_CLUSTER='Cluster'

WLS_ADMIN_T3_URL='t3://localhost:7001'
WLS_ADMIN_HOST='localhost'
WLS_ADMIN_PORT=7001
WLS_ADMIN_SERVER_NAME='AdminServer'