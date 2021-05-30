FROM centos:latest

LABEL Maintainer="Aman Jhagrolia" Technology="Machine Learning" Type="Regression"

WORKDIR /var/lib/ml/
COPY /MLProgram/ /var/lib/ml/

RUN echo "Setting Up Environment..." ; \
    yum install python3 -y &> /dev/null ; \
    python3 -m pip install -r requirements.txt &> /dev/null ; \
    chmod +x predict.py ; \
    echo "Training Model..." ; \
    python3 train_model.py

ENTRYPOINT ["/var/lib/ml/predict.py"]
CMD ["None"]
