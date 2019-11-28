FROM postgres:9.4

ENV POSTGRES_USER=root \
    POSTGRES_PASSWORD=PASSWORD \
    POSTGRES_DB=ehr

EXPOSE 5432/tcp

# And add ``listen_addresses`` to ``/etc/postgresql/postgresql.conf``
RUN echo "listen_addresses='*'" >> /etc/postgresql/postgresql.conf