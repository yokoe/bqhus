FROM python:3.8
WORKDIR /code
COPY . .
RUN pip install -r requirements.txt
RUN pip install -r dev-requirements.txt

CMD ["sh", "run_test.sh"]
