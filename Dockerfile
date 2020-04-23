FROM python:3.7-slim

RUN apt-get update && apt-get install -yqq cron curl libgomp1

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

RUN pip install dagit dagster_postgres dagster_cron ipdb xgboost

WORKDIR /opt/dagster/startup

COPY utils/entrypoint.sh .

RUN chmod +x entrypoint.sh 

EXPOSE 3000

WORKDIR /opt/dagster/pipelines

ENV PYTHONBREAKPOINT=ipdb.set_trace
ENV PYTHONDONTWRITEBYTECODE=1

ENTRYPOINT ["/opt/dagster/startup/entrypoint.sh"]

HEALTHCHECK CMD curl -f http://localhost:3000/dagit_info || exit 1
