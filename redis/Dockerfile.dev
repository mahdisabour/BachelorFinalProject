FROM redis
COPY redis.conf /usr/local/etc/redis/redis.conf
RUN chmod 644 /usr/local/etc/redis/redis.conf
RUN chmod 644 /etc/
CMD [ "redis-server", "/usr/local/etc/redis/redis.conf" ]