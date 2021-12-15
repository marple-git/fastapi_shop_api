# FastAPI + SQLModel + Alembic

Sample FastAPI project that uses async SQLAlchemy, SQLModel, Postgres, Alembic, and Docker.

## Want to use this project?

```sh
$ docker-compose up -d --build
$ docker-compose exec web alembic upgrade head
```

Sanity check: [http://localhost:8004/ping](http://localhost:8004/ping)
