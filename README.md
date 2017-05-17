cd /mnt/d/Archive/Projects/Clients/RMD/RobertMillerDesigner.com

dev_appserver.py app.yaml

gcloud auth login
gcloud config set project rmd2-1037
gcloud app deploy app.yaml index.yaml

gcloud app browse
