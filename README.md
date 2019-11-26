# Python REST API Container

A starting base for running a [Falcon API](https://falcon.readthedocs.io/en/stable/) in a container on the cloud.

## Features

- Generates a self-signed certificate to encrypt traffic between load balancers and the back-end instance.
- Moves gunicorn's directory for worker heartbeats to `/dev/shm`. See https://pythonspeed.com/articles/gunicorn-in-docker/ for why this is important.
- Uses `pipenv` to create a virtual environment that is installed system-wide in the container.
- Resulting image is only 150 MB.
- Contains some sane defaults for gunicorn.
