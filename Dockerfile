FROM python:3.14

# Mounts the application code to the image
COPY . code
WORKDIR /code
RUN pip3 install .

RUN mkdir -p /code/src/resources
# The container would require a volume on that path.
VOLUME /code/src/resources

EXPOSE 80

# runs the production server
ENTRYPOINT ["uvicorn", "webapi.main:app"]
CMD ["--host", "0.0.0.0", "--port", "80"]