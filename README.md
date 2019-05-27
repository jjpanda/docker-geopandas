docker run --rm  --env="DISPLAY" -v /${PWD}:/data jjpan/geopandastest

docker run -t -d  --name conda1 jjpan/geopandastest

docker run -t -d --name conda01 -v //C/Temp:/app/data jjpan/geopandastest

docker volume create --name datafile

docker exec -it conda2 bash


docker run --name conda01 -d -t -v /$(pwd):/app/data jjpan/geopandastest

docker exec -it conda2 bash

docker build -t jjpan/geopandastest .