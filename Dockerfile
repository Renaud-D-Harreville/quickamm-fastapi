FROM python:3.14

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Mounts the application code to the image
COPY . code
WORKDIR /code
RUN pip3 install -e .

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "-m", "uvicorn"]
CMD ["webapi.main:app", "--reload"]