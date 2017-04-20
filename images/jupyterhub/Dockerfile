#
# Image for the jupyterhub service with EGI CheckIn authentication and
# Kubernetes Spawner
# Based on https://github.com/GoogleCloudPlatform/gke-jupyter-classroom
#

FROM jupyterhub/jupyterhub:0.7.2

LABEL maintainer "enol.fernandez@egi.eu"

WORKDIR /opt

# TODO: consider migrating to jupyterhub/kubespawner
RUN apt-get -qq update && apt-get install -y nfs-common \
    && pip install requests-futures \
           git+git://github.com/sveesible/jupyterhub-kubernetes-spawner.git \
           git+git://github.com/enolfc/oauthenticator.git \
    && openssl rand -hex 1024 > configproxy.token \
    && openssl rand -hex 32 > cookie.secret \
    && mkdir -p /mnt/jupyterhub \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+rx /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [""]
