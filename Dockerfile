FROM python:3
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 8000

ENV REGISTRATION_SECRET=stc4lyfe

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=wwustc.dev-settings"]
