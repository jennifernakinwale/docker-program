

FROM python:3.9.10-alpine as build

COPY script.py "/home/data/script.py"


WORKDIR "/home/data"


ENTRYPOINT ["python", "script.py"]