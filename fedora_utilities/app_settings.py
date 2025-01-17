"""
 mod:`app_settings` Fedora Batch App Settings
"""
import sys,os
import aristotle.settings as settings
#from eulfedora.server import Repository
#print(os.path.join(settings.PROJECT_HOME,"aristotle/lib/"))
#sys.path.append(os.path.join(settings.PROJECT_HOME,"aristotle/lib/"))

#from fcrepo.http.restapi import FCRepoRestAPI
try:
    from aristotle.settings import FEDORA_URL,FEDORA_USERNAME,FEDORA_PASSWORD,FEDORA_NAMESPACE
except:
    FEDORA_URL = 'http://127.0.0.1/fedora/'
    FEDORA_USERNAME = 'fedoraAdmin'
    FEDORA_PASSWORD = 'fedora'
    FEDORA_NAMESPACE = 'fedora'
    

APP = {'current_view': {'title':'Fedora Utilities'},
       'description': 'The Fedora Utilities App contains helper functions for assisting in the management of a Fedora Commons Repository.',
       'icon_url':'fedora-commons.png',
       'productivity':True,
       'url':'fedora_utilities/'}

##fedora_repo = FCRepoRestAPI(repository_url=FEDORA_URL,
##                            namespace= FEDORA_NAMESPACE,
##                            username=FEDORA_USERNAME,
##                            password=FEDORA_PASSWORD)
                            
#fedora_repo = Repository()
fedora_repo = None
