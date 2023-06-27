#!/usr/bin/env/bash

# Let DB start
python ./app/backend_pre_start.py

# Run migrations
alembic upgrade head

# create initial data
python ./app/initial_data.py