FROM python
WORKDIR /app
COPY . .
RUN pip install grpcio grpcio-tools pydantic
ENV PYTHONPATH=/app
CMD ["python", "server.py"]
