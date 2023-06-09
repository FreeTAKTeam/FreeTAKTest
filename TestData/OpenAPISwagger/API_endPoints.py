@app.route(/locate/api', methods=["
@app.route('/Marti/api/activeconnections', methods=["
@app.route('/Marti/api/authentication/config', methods=["
@app.route('/Marti/api/cachedConfig', methods=["
@app.route('/Marti/api/cachedInputConfig', methods=["
@app.route('/Marti/api/caveat', methods=["
@app.route('/Marti/api/caveat/<name>', methods=["
@app.route('/Marti/api/certadmin/cert', methods=["
@app.route('/Marti/api/certadmin/cert/<hash>', methods=["
@app.route('/Marti/api/certadmin/cert/<hash>/download', methods=["
@app.route('/Marti/api/certadmin/cert/active', methods=["
@app.route('/Marti/api/certadmin/cert/delete/<ids>', methods=["
@app.route('/Marti/api/certadmin/cert/download/<ids>', methods=["
@app.route('/Marti/api/certadmin/cert/expired', methods=["
@app.route('/Marti/api/certadmin/cert/replaced', methods=["
@app.route('/Marti/api/certadmin/cert/revoke/<ids>', methods=["
@app.route('/Marti/api/certadmin/cert/revoked', methods=["
@app.route('/Marti/api/citrap', methods=["
    """
    citrap (Situation Reports?) supports the plugin for called "Reports"
    """
@app.route('/Marti/api/citrap/<id>', methods=["
@app.route('/Marti/api/citrap/<id>/attachment', methods=["
    """
   Classification (???)
    """
@app.route('/Marti/api/classification', methods=["
@app.route('/Marti/api/classification/<level>', methods=["
@app.route('/Marti/api/clearFederationEvents', methods=["
@app.route('/Marti/api/clientEndPoints', methods=["
@app.route('/Marti/api/config', methods=["
@app.route('/Marti/api/contacts/all', methods=["
@app.route('/Marti/api/cops', methods=["
@app.route('/Marti/api/cops/hierarchy', methods=["
@app.route('/Marti/api/cot', methods=["
@app.route('/Marti/api/cot/sa', methods=["
@app.route('/Marti/api/cot/search/<id>', methods=["
@app.route('/Marti/api/cot/search/date', methods=["
@app.route('/Marti/api/cot/xml/<uid>', methods=["
@app.route('/Marti/api/cot/xml/<uid>/all', methods=["
@app.route('/Marti/api/database/cotCount', methods=["
@app.route('/Marti/api/datafeeds', methods=["
@app.route('/Marti/api/datafeeds/<name>', methods=["
@app.route('/Marti/api/device/profile', methods=["
@app.route('/Marti/api/device/profile/<id>', methods=["
@app.route('/Marti/api/device/profile/<name>', methods=["
@app.route('/Marti/api/device/profile/<name>/directories', methods=["
@app.route('/Marti/api/device/profile/<name>/directories/<directories>', methods=["
@app.route('/Marti/api/device/profile/<name>/file', methods=["
@app.route('/Marti/api/device/profile/<name>/file/<id>', methods=["
@app.route('/Marti/api/device/profile/<name>/files', methods=["
@app.route('/Marti/api/device/profile/<name>/missionpackage', methods=["
@app.route('/Marti/api/device/profile/<name>/send', methods=["
@app.route('/Marti/api/device/profile/connection', methods=["
@app.route('/Marti/api/device/profile/directories', methods=["
@app.route('/Marti/api/device/profile/tool/<toolName>', methods=["
@app.route('/Marti/api/device/profile/tool/<toolName>/file', methods=["
    """
    The Execution Checklist (ExCheck) allows users to monitor and update the status of a shared 
    checklist that is hosted out on a TAK server. Each checklist is an instance of a template 
    that defines a number of tasks to be completed. 
    """
@app.route('/Marti/api/excheck/<checklistUid>/stop', methods=['POST'])
@app.route('/Marti/api/excheck/<templateUid>/start', methods=['POST'])
@app.route('/Marti/api/excheck/checklist', methods=['POST'])
@app.route('/Marti/api/excheck/checklist/<checklistUid>', methods=['GET'])
@app.route('/Marti/api/excheck/checklist/<checklistUid>/mission/<missionName>', methods=['PUT', 'DELETE'])
@app.route('/Marti/api/excheck/checklist/<checklistUid>/status', methods=['GET', 'DELETE'])
@app.route('/Marti/api/excheck/checklist/<checklistUid>/task/<taskUid>', methods=['GET', 'PUT','DELETE'])
@app.route('/Marti/api/excheck/checklist/active', methods=['GET'])
@app.route('/Marti/api/excheck/template', methods=['POST'])
@app.route('/Marti/api/excheck/template/<templateUid>', methods=['GET', 'DELETE'])
@app.route('/Marti/api/excheck/template/<templateUid>/task/<taskUid>', methods=['GET', 'PUT','DELETE','POST'])
    """
        The federation function allows  to connect to another server of the TAK family and exchange information such as COT and chats. 
        
    """
@app.route('/Marti/api/federatecagroups', methods=["
@app.route('/Marti/api/federatecagroups/<caId>', methods=["
@app.route('/Marti/api/federatecertificates', methods=["
@app.route('/Marti/api/federatecertificates/<fingerprint>', methods=["
@app.route('/Marti/api/federatecontacts/<federateId>', methods=["
@app.route('/Marti/api/federatedetails', methods=["
@app.route('/Marti/api/federatedetails/<federateId>', methods=["
@app.route('/Marti/api/federatedetails/<id>', methods=["
@app.route('/Marti/api/federategroupconfig', methods=["
@app.route('/Marti/api/federategroups', methods=["
@app.route('/Marti/api/federategroups/<federateId>', methods=["
@app.route('/Marti/api/federategroupsmap/<federateId>', methods=["
@app.route('/Marti/api/federateremotegroups/<federateId>', methods=["
@app.route('/Marti/api/federates', methods=["
@app.route('/Marti/api/federationconfig', methods=["
@app.route('/Marti/api/federationconfig/verify', methods=["
@app.route('/Marti/api/fednum', methods=["
    """
        Internal API
    """
@app.route('/Marti/api/groupprefix', methods=["
@app.route('/Marti/api/groups', methods=["
@app.route('/Marti/api/groups/<name>/<direction>', methods=["
@app.route('/Marti/api/groups/active', methods=['PUT'])
@app.route('/Marti/api/groups/activebits', methods=['PUT'])
@app.route('/Marti/api/groups/all', methods=["
@app.route('/Marti/api/groups/groupCacheEnabled', methods=["
@app.route('/Marti/api/groups/members', methods=["
@app.route('/Marti/api/groups/update/<username>', methods=['GET'
@app.route('/Marti/api/home', methods=["
@app.route('/Marti/api/icon/<uid>/<group>/<name>', methods=["
@app.route('/Marti/api/iconimage', methods=["
@app.route('/Marti/api/iconset', methods=["
@app.route('/Marti/api/iconset/all/uid', methods=["
@app.route('/Marti/api/iconseturl/<uid>', methods=["
@app.route('/Marti/api/iconurl', methods=["
@app.route('/Marti/api/injectors/cot/uid', methods=["
@app.route('/Marti/api/injectors/cot/uid/<uid>', methods=["
@app.route('/Marti/api/inputs', methods=["
@app.route('/Marti/api/inputs/<id>', methods=["
@app.route('/Marti/api/inputs/<name>', methods=["
@app.route('/Marti/api/inputs/config', methods=["
@app.route('/Marti/api/inputs/storeForwardChat/disable', methods=["
@app.route('/Marti/api/inputs/storeForwardChat/enable', methods=["
@app.route('/Marti/api/inputs/storeForwardChat/enabled', methods=["
@app.route('/Marti/api/maplayers', methods=["
@app.route('/Marti/api/maplayers/<uid>', methods=["
@app.route('/Marti/api/maplayers/all', methods=["
    """
       The Data Synchronizationis used to synchronize multiple TAK clients involved in the same exercise or event. 
    """
@app.route('/Marti/api/missions', methods=['GET'])
@app.route('/Marti/api/missions/<childName>/parent', methods=['DELETE'])
@app.route('/Marti/api/missions/<childName>/parent/<parentName>', methods=['PUT'])
@app.route('/Marti/api/missions/<missionName>/copy', methods=['PUT'])
@app.route('/Marti/api/missions/<missionName>/feed', methods=['POST']) 
@app.route('/Marti/api/missions/<missionName>/feed/<uid>', methods=['DELETE'])
@app.route('/Marti/api/missions/<missionName>/invitations', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/log', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/maplayers', methods=['PUT','POST'])
@app.route('/Marti/api/missions/<missionName>/maplayers/<uid>', methods=['DELETE'])
@app.route('/Marti/api/missions/<missionName>/role', methods=['GET', 'PUT'])
@app.route('/Marti/api/missions/<missionName>/subscription', methods=['GET', 'PUT', 'POST', 'DELETE'])
@app.route('/Marti/api/missions/<missionName>/subscriptions', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/subscriptions/roles', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/token', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/Marti/api/missions/<missionName>/archive', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/changes', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/children', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/contacts', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/content/<hash>/keywords', methods=['PUT', 'DELETE', 'GET'])
@app.route('/Marti/api/missions/<missionName>/contents', methods=['PUT','DELETE'])
@app.route('/Marti/api/missions/<missionName>/contents/missionpackage', methods=['PUT'])
@app.route('/Marti/api/missions/<missionName>/cot', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/expiration', methods=['PUT'])
@app.route('/Marti/api/missions/<missionName>/externaldata', methods=['POST'])
@app.route('/Marti/api/missions/<missionName>/externaldata/<id>', methods=['DELETE'
@app.route('/Marti/api/missions/<missionName>/externaldata/<id>/change', methods=['POST'])
@app.route('/Marti/api/missions/<missionName>/invite', methods=['POST'])
@app.route('/Marti/api/missions/<missionName>/invite/<type>/<invitee>', methods=['PUT', 'DELETE'])
@app.route('/Marti/api/missions/<missionName>/keywords', methods=['PUT', 'DELETE'])
@app.route('/Marti/api/missions/<missionName>/keywords/<keyword>', methods=['DELETE'])
@app.route('/Marti/api/missions/<missionName>/kml', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/parent', methods=['GET'])
@app.route('/Marti/api/missions/<missionName>/password', methods=['DELETE', 'PUT'])
@app.route('/Marti/api/missions/<missionName>/send', methods=['POST'])
@app.route('/Marti/api/missions/<missionName>/uid/<uid>/keywords', methods=['PUT','DELETE'])
@app.route('/Marti/api/missions/all/invitations', methods=['GET'])
@app.route('/Marti/api/missions/all/logs', methods=['GET'])
@app.route('/Marti/api/missions/all/subscriptions', methods=['GET'])
@app.route('/Marti/api/missions/invitations', methods=['GET'])
@app.route('/Marti/api/missions/logs/entries', methods=['PUT','POST'])
@app.route('/Marti/api/missions/logs/entries/<id>', methods=['GET','DELETE' ])
    """
        Internal API
    """
@app.route('/Marti/api/node/id', methods=["
@app.route('/Marti/api/outgoingconnections', methods=["
@app.route('/Marti/api/outgoingconnections/<name>', methods=["
@app.route('/Marti/api/outgoingconnectionstatus/<name>', methods=["
    """
        Internal API
    """
@app.route('/Marti/api/plugins/<name>/submit', methods=["
@app.route('/Marti/api/plugins/<name>/submit/result', methods=["
@app.route('/Marti/api/plugins/info/all', methods=["
@app.route('/Marti/api/plugins/info/all/started', methods=["
@app.route('/Marti/api/plugins/info/archive', methods=["
@app.route('/Marti/api/plugins/info/enabled', methods=["
@app.route('/Marti/api/plugins/info/started', methods=["
@app.route('/Marti/api/properties/<uid>', methods=["
@app.route('/Marti/api/properties/<uid>/<key>', methods=["
@app.route('/Marti/api/properties/<uid>/all', methods=["
@app.route('/Marti/api/properties/uids', methods=["
    """
        Internal API
    """
@app.route('/Marti/api/qos/conf', methods=["
@app.route('/Marti/api/qos/delivery/enable', methods=["
@app.route('/Marti/api/qos/dos/enable', methods=["
@app.route('/Marti/api/qos/ratelimit/delivery/active', methods=["
@app.route('/Marti/api/qos/ratelimit/dos/active', methods=["
@app.route('/Marti/api/qos/ratelimit/read/active', methods=["
@app.route('/Marti/api/qos/read/enable', methods=["
    """
        Streams a certain COT to all the clients
    """
@app.route('/Marti/api/repeater/list', methods=["
@app.route('/Marti/api/repeater/period', methods=["
@app.route('/Marti/api/repeater/remove/<uid>', methods=['GET'
@app.route('/Marti/api/resources/<hash>', methods=["
@app.route('/Marti/api/security/config', methods=["
@app.route('/Marti/api/security/isSecure', methods=["
@app.route('/Marti/api/security/verifyConfig', methods=["
  """
    subscription-api
    """
@app.route('/Marti/api/subscriptions/<clientUid>/filter', methods=['PUT', 'DELETE',
@app.route('/Marti/api/subscriptions/add', methods=["'POST'
@app.route('/Marti/api/subscriptions/all', methods=['GET'
@app.route('/Marti/api/subscriptions/delete/<uid>', methods=[''DELETE''
@app.route('/Marti/api/subscriptions/incognito/<uid>', methods=["'POST'
   """
    syncronize metadata
    """
@app.route('/Marti/api/sync/metadata/<hash>/<metadata>', methods=['PUT'
@app.route('/Marti/api/sync/metadata/<hash>/expiration', methods=['PUT'
@app.route('/Marti/api/sync/metadata/<hash>/keywords', methods=['PUT'

@app.route('/Marti/api/sync/search', methods=['GET'
@app.route('/Marti/api/sync/sequence/<key>', methods=["
@app.route('/Marti/api/tls/config', methods=["
@app.route('/Marti/api/tls/makeClientKeyStore', methods=["
@app.route('/Marti/api/tls/profile/enrollment', methods=["
@app.route('/Marti/api/tls/profile/tool/<toolName>/file', methods=["
@app.route('/Marti/api/tls/signClient', methods=["
@app.route('/Marti/api/tls/signClient/v2', methods=["
@app.route('/Marti/api/token', methods=["
@app.route('/Marti/api/token/<token>', methods=["
@app.route('/Marti/api/token/revoke/<tokens>', methods=["
@app.route('/Marti/api/uidsearch', methods=["
@app.route('/Marti/api/users/<connectionId>', methods=["
@app.route('/Marti/api/users/all', methods=["
@app.route('/Marti/api/util/isAdmin', methods=["
@app.route('/Marti/api/util/user/roles', methods=["
   """
   
    """
@app.route('/Marti/api/ver', methods=["
@app.route('/Marti/api/version', methods=["
@app.route('/Marti/api/version/config', methods=["
@app.route('/Marti/api/version/info', methods=["
    """
        video-connection-manager-v-2 (since TAK Server 4.8
        Manage informations related to video feeds (not the video itself 
    """
@app.route('/Marti/api/video', methods=['GET','POST' 
@app.route('/Marti/api/video/<uid>', methods=['GET','DELETE',PUT

   """
   
    """
@app.route('/register/admin/invite', methods=["
@app.route('/register/admin/users', methods=["
@app.route('/register/token/<token>', methods=["
@app.route('/register/user', methods=["
    """
    file-user-account-management-api
    """
@app.route('/user-management/api/change-user-password', methods=['PUT'
@app.route('/user-management/api/delete-user/<username>', methods=['DELETE'
@app.route('/user-management/api/get-groups-for-user/<username>', methods=['GET'
@app.route('/user-management/api/list-groupnames', methods=['GET'
@app.route('/user-management/api/list-users', methods=['GET'
@app.route('/user-management/api/new-user', methods=["'POST'
@app.route('/user-management/api/new-users', methods=["'POST'
@app.route('/user-management/api/update-groups', methods=['PUT'
@app.route('/user-management/api/users-in-group/<group>', methods=['GET'
    """
    file-user-account-management-api
    """
@app.route('/vbm/api/config', methods=["
@app.route('vbm/api/config', methods=["

"""
    xmpp-api
    Manages files transfer over the XMMP protocol, works only with the proper plugin
"""
@app.route('/Marti/api/xmpp/transfer/{uid}/{filename}', methods=['GET'
@app.route('/Marti/api/xmpp/transfer/{uid}/{filename}', methods=['PUT'
@app.route('/Marti/api/xmpp/transfer/<uid>/<filename>', methods=["