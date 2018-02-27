FROM python:3
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "run:app", "-w 4", "-b 0.0.0.0:8000"]