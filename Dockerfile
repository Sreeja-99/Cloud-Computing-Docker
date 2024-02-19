# Use a minimal base image: Linux apline 
FROM alpine:latest

# Install necessary packages: Python installation
RUN apk add --no-cache python3

# Set the working directory inside the container
WORKDIR /home

# Create the output directory
RUN mkdir -p /home/output

# Copy the Python script and input files into the container
COPY myPythonScript.py /home

#Copying entire files of the directory present in host machine to /home/data directory of the container
COPY . /home/data

#Copying individual files present in host machine to /home/data directory of the container
#COPY /IF.txt /home/data/
#COPY /Limerick-1.txt /home/data/

# Run the Python script when the container starts
CMD ["python3", "/home/myPythonScript.py"]

