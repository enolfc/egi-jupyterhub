#
# Image for the jupyterhub service with EGI CheckIn authentication and
# Kubernetes Spawner
# Based on https://github.com/GoogleCloudPlatform/gke-jupyter-classroom
#

FROM jupyterhub/jupyterhub:0.7.2

LABEL maintainer "enol.fernandez@egi.eu"

WORKDIR /opt

RUN apt-get -qq update && apt-get install -y nfs-common \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# TODO: consider migrating to jupyterhub/kubespawner
RUN pip install requests-futures \
                git+https://github.com/enolfc/oauthenticator.git \
                git+https://github.com/enolfc/kubespawner.git \
    && openssl rand -hex 1024 > configproxy.token \
    && openssl rand -hex 32 > cookie.secret \
    && mkdir -p /mnt/jupyterhub

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+rx /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD [""]
