FROM python:3.8-alpine

WORKDIR /brain-games

COPY dist/hexlet_code-0.3.0-py3-none-any.whl /brain-games

RUN python3 -m pip install hexlet_code-0.3.0-py3-none-any.whl --force
