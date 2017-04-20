# 
# Configuration for the EGI Jupyterhub
#

c = get_config()

import os

c.JupyterHub.log_level = os.environ.get('JHUB_LOG_LEVEL', 'DEBUG')

c.JupyterHub.proxy_api_ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.extra_log_file = '/var/log/jupyterhub.log'
#allows admin to log in to user instances
c.JupyterHub.admin_access = True
#c.Authenticator.admin_users = admin = set()
#admin.update(os.environ['ADMIN_USERS'].split(','))
# c.Authenticator.whitelist = whitelist = set()
#whitelist.update(os.environ['OAUTH_WHITELIST'].split(','))

# Authentication
c.JupyterHub.authenticator_class = 'oauthenticator.EGICheckInOAuthenticator'
c.EGICheckInOAuthenticator.client_id = os.environ.get('OAUTH_CLIENT_ID', '')
c.EGICheckInOAuthenticator.client_secret = os.environ.get('OAUTH_CLIENT_SECRET', '')
c.EGICheckInOAuthenticator.oauth_callback_url = os.environ.get('OAUTH_CALLBACK_URL', '')


# Spawner Options
c.JupyterHub.spawner_class = 'kubernetespawner.Kubernetespawner'
c.Kubernetespawner.start_timeout = 50
c.Kubernetespawner.debug = os.environ.get('JHUB_SPWN_DEBUG', '') == "TRUE"
c.Kubernetespawner.pod_name_template = 'jupyter-{userid}-notebook'
c.Kubernetespawner.hub_ip_connect = os.environ.get('KSPAWN_HUB_IP', None)
c.Kubernetespawner.kube_namespace = 'jupyterhub'
c.Kubernetespawner.singleuser_image_spec = os.environ.get('KUBESPAWN_IMAGE',
                                                          None)
c.Kubernetespawner.use_options_form = False
c.Kubernetespawner.cpu_limit = os.environ.get('KUBESPAWN_CPU_LIMIT', None)
c.Kubernetespawner.cpu_request = os.environ.get('KUBESPAWN_CPU_REQUEST', None)
c.Kubernetespawner.mem_limit = os.environ.get('KUBESPAWN_MEM_LIMIT', None)
c.Kubernetespawner.mem_request = os.environ.get('KUBESPAWN_MEM_REQUEST', None)
c.Kubernetespawner.notebook_dir = '/mnt/notebooks'
c.Kubernetespawner.create_user_volume_locally = True
c.Kubernetespawner.volumes = [
    {"name": "{userid}-nfs",
     "nfs": {"path": os.environ.get('KUBESPAWN_NFS_PATH', ''),
             "server": os.environ.get('KUBESPAWN_NFS_SERVER', '')}
    }
]
c.Kubernetespawner.volume_mounts = [{"name": "{userid}-nfs",
                                     "mountPath": "/mnt/notebooks"} ]
c.Kubernetespawner.http_timeout = 60
