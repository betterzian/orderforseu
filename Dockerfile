FROM selenium/standalone-chrome:104.0-chromedriver-104.0
USER root
ENV TZ=Asia/Shanghai \
    DEBIAN_FRONTEND=noninteractive

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get update \
    && apt-get install -y python3-pip \
    && pip3 install selenium==3.141.0 \
    && mkdir /usr/share/mypython \
    && mkdir /usr/share/mypython/data
VOLUME /usr/share/mypython/data
ADD login.py /usr/share/mypython
ADD userdata.py /usr/share/mypython
WORKDIR /usr/share/mypython
CMD python3 login.py