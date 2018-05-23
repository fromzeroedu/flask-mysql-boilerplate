FROM python:3.4.5-slim

## make a local directory
RUN mkdir /counter_app

# set "counter_app" as the working directory from which CMD, RUN, ADD references
WORKDIR /counter_app

# now copy all the files in this directory to /code
ADD . .

# pip install the local requirements.txt
RUN pip install -r requirements.txt

# Listen to port 5000 at runtime
EXPOSE 5000

# Define our command to be run when launching the container
CMD flask run --host 0.0.0.0
