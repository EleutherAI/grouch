FROM continuumio/miniconda3

WORKDIR /workspace
ADD requirements.txt .
RUN pip install -r requirements.txt
ADD . .
EXPOSE 5000
ENV APP_PATH /workspace
CMD python runapp.py