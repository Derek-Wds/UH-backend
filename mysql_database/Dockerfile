FROM mysql/mysql-server:latest

ENV MYSQL_USER=mysql \
    MYSQL_DATA_DIR=/var/lib/mysql \
    MYSQL_RUN_DIR=/run/mysqld \
    MYSQL_LOG_DIR=/var/log/mysql \
    MYSQL_ROOT_PASSWORD=PASSWORD

EXPOSE 3306/tcp

ENTRYPOINT ["/entrypoint.sh"]

CMD ["mysqld"]