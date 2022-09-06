FROM selenium/standalone-chrome:104.0-chromedriver-104.0
USER root
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install selenium==3.141.0
RUN mkdir /usr/share/mypython
RUN mkdir /usr/share/mypython/data
VOLUME /usr/share/mypython/data
ADD login.py /usr/share/mypython
ADD userdata.py /usr/share/mypython
WORKDIR /usr/share/mypython
CMD python3 login.py