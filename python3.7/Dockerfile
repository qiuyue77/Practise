FROM qiuyue77/python3.7:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements /code/requirements
# RUN apt-get update && apt-get -y install supervisor fabric
RUN pip install -r requirements/base.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
