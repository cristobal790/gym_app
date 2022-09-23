FROM python:3.9.14-alpine

RUN mkdir /app

ADD requirements.txt /app/requirements.txt

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev build-base \
    && apk add libffi-dev\
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /app/requirements.txt \
    && runDeps="$(scanelf --needed --nobanner --recursive /env \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps

#ADD Plataforma_myra /app

#RUN rm /etc/nginx/conf.d/default.conf
COPY /nginx/default.conf /etc/nginx/conf.d/default.conf
ADD entrypoint.sh /app/entrypoint.sh


WORKDIR /app


ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]