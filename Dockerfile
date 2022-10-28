FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

RUN apt update -y && \
    apt install -y python3-pip libc6-dbg gdb cmake libgtest-dev
RUN pip install cpplint Django
RUN wget https://sourceware.org/pub/valgrind/valgrind-3.18.1.tar.bz2 && \
    tar xfv valgrind-3.18.1.tar.bz2 && \
    cd valgrind-3.18.1 && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install