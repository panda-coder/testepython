FROM debian:9.9-slim

LABEL maintainer="Ercy Moreira Neto <fireball.vb>"

WORKDIR /app

RUN apt-get update -yq
RUN apt-get install -y python3 python3-pip

ARG INSTALL_DJANGO=false
ENV INSTALL_DJANGO ${INSTALL_DJANGO}

RUN if [ ${INSTALL_DJANGO} = true ]; then \
    # run the install
    pip3 install Django \
;fi





