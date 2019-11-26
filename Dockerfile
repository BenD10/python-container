# Generate a self-signed cert to be copied into the final container.
FROM alpine:3.10 as ssl
RUN apk add openssl && \
    openssl req -newkey rsa:2048 -nodes -batch -x509 -days 90 -keyout /tmp/ssl.key -out /tmp/ssl.crt

FROM python:3.8-alpine
COPY --from=ssl --chown=100:100 /tmp/ssl.key /etc/ssl/private/ssl.key
COPY --from=ssl --chown=100:100 /tmp/ssl.crt /etc/ssl/certs/ssl.crt

# Install all dependencies first, since they're likely to be cached.
COPY Pipfile* /
RUN pip install pipenv && \
    pipenv install --system --deploy

# Switch to a new user that isn't root, and copy in source.
USER 100:100
COPY ./app app
WORKDIR /app

# Start gunicorn when the container starts.
CMD ["gunicorn", "-c", "gunicorn.conf.py", "app:app"]