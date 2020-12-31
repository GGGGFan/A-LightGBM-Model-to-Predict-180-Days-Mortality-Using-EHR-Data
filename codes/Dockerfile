FROM python:3.7

# Install dependencies
RUN pip install pandas \
  numpy \
  sklearn \
  datetime \
  joblib \
  matplotlib \
  lightgbm \
  scipy==1.3.0\
  optuna

# Move to the app folder
RUN mkdir /app
WORKDIR /app

# Copy our python program for training and inference
COPY ./train.py .
COPY ./infer.py .
COPY ./helpers.py .
COPY ./dream_challenge_3.sqlite3 .
COPY ./measurement_query.txt .
COPY ./measurement_evl_query.txt .

# Copy Bash scripts expected by the IT infrastructure of the EHR DREAM Challenge
COPY ./train.sh .
COPY ./infer.sh .

# Add executable permission to Bash scripts
RUN chmod +x train.sh infer.sh
