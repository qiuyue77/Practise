FROM python:3.8.2
MAINTAINER qiujl qiuyue77@outlook.com
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements /code/requirements
#RUN apt-get update && apt-get -y install supervisor fabric vim
RUN pip install -r requirements/base.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
