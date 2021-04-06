# base image
FROM python:3.7.5-slim
RUN pip3 install --upgrade pip

# make a folder to work in
RUN mkdir /project/

# copy over what we need
COPY deploy/ /project/deploy/
COPY package /project/package/
COPY main.py /project/main.py
RUN python3 -m pip install -r /project/deploy/requirements.txt


WORKDIR /project/
EXPOSE 1313
CMD ["python3", "main.py"]
