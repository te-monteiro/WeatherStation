FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED=1
RUN pip install pandas
RUN pip install pytest-django
RUN pip install django-timed-tests
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

