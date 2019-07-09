FROM continuumio/miniconda3

#LABEL maintainer="random"

RUN conda config --add channels conda-forge && conda update -y conda \
    && conda install -y geopandas contextily matplotlib geoplot

WORKDIR /app

COPY . .

CMD ["python", "test.py"]