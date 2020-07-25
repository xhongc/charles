FROM nginx


#对外暴露端口
EXPOSE 80 8088

ADD nginx.conf  /etc/nginx/conf.d/

RUN mkdir -p /usr/share/nginx/html/static
RUN mkdir -p /usr/share/nginx/html/media
