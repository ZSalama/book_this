ARG PYTHON_VERSION=3.12.6
FROM python:${PYTHON_VERSION}

# create virtual env
RUN python -m venv /opt/venv

# Set virtual env path
ENV PATH=/opt/venv/bin:$PATH

RUN pip install --upgrade pip

# set python env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install os dependencies for mini vm
RUN apt-get update && apt-get install -y \
    # postgres
    libpq-dev \
    #pillow
    libjpeg-dev \
    #cairoSVG
    libcairo2 \
    #other
    gcc \
    && rm -rf /var/lib/apt/lists/*

#create mini vm's code dir
RUN mkdir -p /code

#set working directory
WORKDIR /code

#copy requirements
COPY requirements/txt /tmp/requirements.txt

#copy project code to containers working directory
COPY ./src /code

#install python project requirements
RUN pip install -r /tmp/requirements.txt

#run any other commands that do not need the database here

#set Django default project name
ARG PROJ_NAME="django_backend"

#create bash script to run django project
RUN prinf "#!/bin/bash\n" > ./paracord_runner.sh && \
    printf "RUN_PORT=\"\${PORT:-8000}\"\n\n" >> ./paracord_runner.sh && \
    printf "python manage.py migrate --noinput\n" >> ./paracord_runner.sh && \
    printf "gunicorn ${PROJ_NAME}.wsgi:application --bind \"0.0.0.0:\$RUN_PORT\"\n" >> ./paracord_runner.sh 

#set bash script permissions
RUN chmod +x paracord_runner.sh

#clean up apt cache
RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#run django project using bash script
CMD ./paracord_runner.sh