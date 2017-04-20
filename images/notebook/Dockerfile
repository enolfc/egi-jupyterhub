#
# Base EGI Jupyterhub container image that adds two kernels to the base
# jupyterhub/singleuser: octave and scilab
#

# TODO: understand if we should use a specific version here
FROM jupyterhub/singleuser:latest

LABEL maintainer "enol.fernandez@egi.eu"

USER root

RUN apt-get update && \
    apt-get install --no-install-recommends -y octave gnuplot \
                                               ghostscript curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

USER $NB_USER

# octave Kernel
RUN conda install --quiet --yes \
    'octave_kernel'  && \
    conda clean -tipsy && \
    python -m octave_kernel.install

# Scilab kernel
RUN curl -L http://www.scilab.org/download/6.0.0/scilab-6.0.0.bin.linux-x86_64.tar.gz | tar -xzf -

ENV SCILAB_EXECUTABLE /home/$NB_USER/work/scilab-6.0.0/bin/scilab

RUN pip3 install scilab_kernel && \
    python -m scilab_kernel.install

# Default CMD coming from jupyterhub/singleuser
CMD ["sh", "/usr/local/bin/start-singleuser.sh"]
