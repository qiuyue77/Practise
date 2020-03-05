FROM python:3.7
MAINTAINER qiujl qiuyue77@outlook.com
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/requirements.txt
# RUN apt-get update && apt-get -y install supervisor fabric
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
