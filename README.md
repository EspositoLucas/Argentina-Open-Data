# Argentina Open Data Challenge

You can find the challenge [here](Challenge.pdf)

## Prerequisites

### Poetry

Poetry is a tool for dependency management and packaging in Python. It allows you to declare the libraries your project depends on and it will manage (install/update) them for you.

You need to install poetry with ```pip install poetry``` then all other dependencies will be managed by it.

Using ```poetry install``` it will create a virtual env with all the necesary dependencies then you can access it with ```poetry shell```.

If you need to add a dependency just use ```poetry add <dependency>``` or you can customice much more editing the ```pyproyect.toml```
I exported all necesary dependencies to a requirements.txt

You can read more about Poetry [here](https://python-poetry.org/)

Also you can expand even further with this post [Hypermodern Python](https://medium.com/@cjolowicz/hypermodern-python-d44485d9d769)


## Data research

You can find the data exploratory research on this [notebook](notebook/data_exploratory.ipynb)

## Setup database

You can setup the dabase by running

```docker run -d --name challenge_pg -v my_dbdata:/var/lib/postgresql/data -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres e POSTGRES_DB=data_analytics postgres```

You can access the database by running

```docker exec -it challenge_pg psql -U postgres -d data_analytics```

## Creating the database

You can create the dabase by running

```python script.py```

This script will read all the files in/challenge/sql/ and run the sql script in them to create each table.

## Running the ETL

First you need to create a settings.ini file. Use the settings.ini.ex for reference You can also set the variables as enviromental vairables by doing

```bash
export DB_CONNSTR=value 
export MUSEO_URL=value
export CINES_URL=value
export ESPACIOS_URL=value
```
Where ```value``` is the correct value you need.

You can run the etl by using the command.

```python python challenge/main.py --date 2024-01-11```
