# Details

## How to use alembic

Context: You have made changes to the sql database. Eg: Added models, schemas, or changed the existing models and schemas

1. Generate the migration script
   - Add changes models to `models/__init__.py`. This ensures that alembic can access the new models
   - run `alembic revision --autogenerate -m "<enter change message here>"` this will generate a migratiin script in versions
   - Look through the files and make sure that changes are correct. Reference for detected and non detected changes [here](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect)
2. Running the migration
   - `alembic upgrade head`
3. Upgrading and downgradinf
   - go to specific version by mentioning the identifier `alembic upgrade ae1` (also supports partial identifiers)
   - Relative identifiers `alembic upgrad +2` or `alembic downgrade -1`
