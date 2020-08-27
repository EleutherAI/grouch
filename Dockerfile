FROM continuumio/miniconda3

WORKDIR /app
ADD requirements.txt /app 
RUN pip install -r requirements.txt
ADD . .
EXPOSE 5000
CMD python runapp.py