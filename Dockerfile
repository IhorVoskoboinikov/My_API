#FROM python:3.10.7-slim
#ENV PYTHONUNBUFFERED 1
#
#EXPOSE 8000
#WORKDIR /app
#
#COPY . .
#
#RUN pip install -e .

FROM python:3.10.7-slim
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . .

ENV PORT 8000

# EXPOSE 8000
EXPOSE $PORT

CMD ["uvicorn", "test_project.app:app"]




