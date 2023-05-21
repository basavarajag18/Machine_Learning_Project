from python =3.7
COPY ./app
WORKDIR /app
run pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn/workers=4 --bind 0.0.0.0:$PORT app:app