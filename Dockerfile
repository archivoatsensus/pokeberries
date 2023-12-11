FROM python:3.10

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /home/www-data && mkdir /home/www-data/app
WORKDIR /home/www-data/app/
COPY *.py ./
EXPOSE 5005

ENV PATH "$PATH:/home/www-data/app/"
ENV PYTHONPATH "${PYTHONPATH}:/home/www-data/app/"

CMD ["python3","app.py"]
