#! /usr/bin/bash

(source $(pwd)/venv/bin/activate && \
cd test_drf && \
pip install -r requirements.txt && \
python3 manage.py collectstatic -c --no-input) && \
sudo docker-compose up --build


