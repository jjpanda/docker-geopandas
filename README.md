# Docker for anaconda::geopandas

### Prerequisites
- Host machine running Docker
- Docker has been configured for windows shared drive
- Install compose if using docker-compose

## Execution Instructions - Docker
```
## Docker build
docker build -t jjpan/geopandastest .

## Docker run
# For windows
docker run --rm --name conda01 -v /$(pwd):/app/data -v /$(pwd)/greetings.txt:/app/data/greetings.txt jjpan/geopandastest

# For linux
docker run --rm --name conda01 -v "$PWD":/app/data -v "$PWD"/greetings.txt:/app/data/greetings.txt jjpan/geopandastest
```
For any changes in test.py, you need to re-execute docker build and then docker run.

## Execution Instructions - docker-compose
```
docker-compose up
docker container ls
```
