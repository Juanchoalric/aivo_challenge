# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

# copy the content of the local src directory to the working directory
COPY app/ .

CMD [ "python", "./app.py" ]