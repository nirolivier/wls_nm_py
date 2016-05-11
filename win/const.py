#   ================================================================
#   This script contains all constants used to connect to the managed
#   server.
#   
#   Author:     Razafindrabekoto Nirina Olivier
#   Date:        09/05/2016
#   Version:    1.0
#   ===============================================================


APP_NAME='myApp'
APP_DEPLOY_PATH_FROM='C:/Users/n.razafindrabekoto/Documents/mydoc/devtools/wls_domain/cleva_deploy/myApp.war'
APP_SERVER_NAME='cleva1'
APP_DOMAIN_NAME='Cleva_dom'
APP_DOMAIN_DIR='C:/Users/n.razafindrabekoto/Documents/mydoc/devtools/wls_domain/Cleva_dom'
APP_DEPLOY_LOG='C:/Users/n.razafindrabekoto/Documents/mydoc/devtools/wls_domain/cleva_deploy/logs/deploy.log'

NM_HOST='localhost'
NM_PORT='5556'
# If you specify plain for nmType, you must manually set the SecureListener parameter in nodemanager.properties to false. 
# Otherwise, the nmConnect command will fail.
NM_TYPE='plain'
NM_HOME='C:/Users/n.razafindrabekoto/Documents/mydoc/devtools/wls1036_dev/wlserver/common/nodemanager'

TYPE_SERVER='Server'
TYPE_CLUSTER='Cluster'

WLS_ADMIN_T3_URL='t3://localhost:7001'
WLS_ADMIN_HOST='localhost'
WLS_ADMIN_PORT=7001
WLS_ADMIN_SERVER_NAME='AdminServer'
