FROM python:3.6.2-slim

ENV DEMO_HOME /app
ENV PATH $DEMO_HOME:$PATH

WORKDIR $DEMO_HOME

COPY demo/ $DEMO_HOME/demo/
COPY setup.py $DEMO_HOME/setup.py

RUN pip install . && \
    rm setup.py

CMD ["gunicorn", "-b 0.0.0.0:8080", "demo.factory:create_app()"]