# Starting with the image used in helm jupyterhub-v0.7-10de8dc
FROM jupyterhub/k8s-hub:10de8dc

USER root
RUN pip3 install git+https://github.com/enolfc/oauthenticator.git@d4science

USER ${NB_USER}
