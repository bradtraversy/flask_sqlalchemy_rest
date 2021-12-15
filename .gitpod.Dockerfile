FROM gitpod/workspace-postgres


RUN pip install -r requirements.txt
RUN python src/main.py