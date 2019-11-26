import os
import multiprocessing

# Controls the number of Gunicorn processes to start. Defaults to recommended value in the docs.
workers = os.getenv('GUNICORN_WORKERS', multiprocessing.cpu_count() * 2 + 1)

# Controls the ports for Gunicorn to bind to.
bind = '0.0.0.0:{}'.format(os.getenv('GUNICORN_PORT', 8000))

# HTTP keepalive timeout in seconds, allows ELBs to reuse back-end connections.
keepalive = 30

# Move the gunicorn heartbeat between workers to an in-memory partition, much faster than writing to disk.
worker_tmp_dir = '/dev/shm'

# SSL configuration so traffic between the load balancer and the app is encrypted.
ssl_version = 'TLSv1_2'
certfile = '/etc/ssl/certs/ssl.crt'
keyfile = '/etc/ssl/private/ssl.key'
