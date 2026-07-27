FROM python:3.14
WORKDIR /code
#RUN apt install python3-flask
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . /code
CMD ["flask", "--app" , "emprunt_api", "run" , "--host" , "0.0.0.0" ]