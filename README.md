# Risk Score and Profile definition

## How to run

There are 2 ways of running this application:

### Docker
To run using docker, simply execute

```
docker-compose up -d
```

### Pipenv

To run using pipenv, execute

```
pip install pipenv
pipenv install --deploy --dev --system --ignore-pipfile
sh entrypoint.sh
```

## Documentation

Once the apllication is running, you can access `http://localhost:5000/apidocs/swagger` or `http://localhost:5000/apidocs/redoc`.

## Main stack

This API was developed using Flask as a web framework and pydantic to manage data validation.