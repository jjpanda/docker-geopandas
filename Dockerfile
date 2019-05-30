FROM continuumio/miniconda3

LABEL maintainer="phua.jj@pg.com"

RUN conda config --add channels conda-forge && conda update -y conda \
    && conda install -y geopandas contextily matplotlib

#RUN mkdir -p /app
WORKDIR /app

COPY test.py test.py

#ENTRYPOINT [ "/usr/bin/tini", "--" ]
#CMD [ "/bin/bash" ]
CMD ["python", "test.py"]