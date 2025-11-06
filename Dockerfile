FROM python:3.14

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code
RUN pip3 install .

EXPOSE 80

# runs the production server
ENTRYPOINT ["uvicorn", "webapi.main:app"]
CMD ["--host", "0.0.0.0", "--port", "80"]