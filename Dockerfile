FROM python:3.10.0 as base

RUN pip install pipenv

ENV PYTHONPATH /srv/src

WORKDIR /srv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --dev --deploy --system --ignore-pipfile

COPY . .

EXPOSE 5000

ENTRYPOINT ["sh", "entrypoint.sh"]