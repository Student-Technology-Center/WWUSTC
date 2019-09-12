FROM python:3
COPY requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /app
COPY . /app
EXPOSE 8000

ENV REGISTRATION_SECRET=stc4lyfe

CMD ["python", "setup.py", "prod"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=wwustc.dev-settings"]
