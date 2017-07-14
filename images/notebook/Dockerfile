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

# Scilab kernel, removed for a while...
#RUN curl -L http://www.scilab.org/download/6.0.0/scilab-6.0.0.bin.linux-x86_64.tar.gz | tar -xzf -

#ENV SCILAB_EXECUTABLE /home/$NB_USER/work/scilab-6.0.0/bin/scilab

#RUN pip3 install scilab_kernel && \
#    python -m scilab_kernel.install



USER root

# FIXME: this should be mounted from NFS
RUN mkdir -p /mnt/notebooks && chown -R $NB_USER /mnt/notebooks

# Upgrade Java
RUN echo "deb http://cdn-fastly.deb.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get install --no-install-recommends -t jessie-backports -y \
                    openjdk-8-jre-headless ca-certificates-java && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
RUN update-alternatives  --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

# Taken from the spark containers at ../spark

ENV hadoop_ver 2.7.3
ENV spark_ver 2.2.0

# Get Hadoop from US Apache mirror and extract just the native
# libs. (Until we care about running HDFS with these containers, this
# is all we need.)
RUN mkdir -p /opt && \
    cd /opt && \
    curl http://www.us.apache.org/dist/hadoop/common/hadoop-${hadoop_ver}/hadoop-${hadoop_ver}.tar.gz | \
        tar -zx hadoop-${hadoop_ver}/lib/native && \
    ln -s hadoop-${hadoop_ver} hadoop && \
    echo Hadoop ${hadoop_ver} native libraries installed in /opt/hadoop/lib/native

# Get Spark from US Apache mirror.
RUN mkdir -p /opt && \
    cd /opt && \
    curl http://www.us.apache.org/dist/spark/spark-${spark_ver}/spark-${spark_ver}-bin-hadoop2.7.tgz | \
        tar -zx && \
    ln -s spark-${spark_ver}-bin-hadoop2.7 spark && \
    echo Spark ${spark_ver} installed in /opt

USER $NB_USER
COPY pyspark /tmp/pyspark
RUN  jupyter kernelspec install --user /tmp/pyspark

#
# Default CMD coming from jupyterhub/singleuser
CMD ["sh", "/usr/local/bin/start-singleuser.sh"]
