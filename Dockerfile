FROM python:3.6
ENV PYTHONUNBUFFERED 1
#更新软件源，必须要执行，否则可能会出错。-y就是要跳过提示直接安装。
RUN apt-get -y update

RUN apt-get install -y python-dev python-pip
RUN apt-get install -y python-setuptools
#MySQL-Python必须得先安装这个库
RUN apt-get install -y default-libmysqlclient-dev

RUN mkdir /webapps
#设置工作目录
WORKDIR /webapps
#将当前目录加入到工作目录中
ADD . /webapps

RUN pip install -r /webapps/requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

EXPOSE 80 8080 8000 8088
