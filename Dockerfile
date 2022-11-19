FROM alpine:latest
RUN apk update && apk add bash

RUN mkdir -p /app
WORKDIR /app
COPY main.py requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "main.py" ]
ENTRYPOINT [ "python" ]