FROM python:3.11.4

WORKDIR /appPrueba

COPY . .
RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"

EXPOSE 8000

RUN pip install -r ./requirements.txt
# CMD ["gunicorn", "main:app", "--workers", "10", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:7000", "--reload"]
CMD ["uvicorn","main:app","--reload","--host","0.0.0.0","--port","8000"]
