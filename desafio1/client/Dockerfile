FROM alpine:latest

RUN apk add --no-cache curl bash

WORKDIR /app

COPY loop.sh .

CMD ["bash", "loop.sh"]
