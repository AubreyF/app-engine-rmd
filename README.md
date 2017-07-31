# RobertMillerDesigner.com

* This repo includes the source code and image assets for RobertMillerDesigner.com.

# App Engine Snippets
```
# Local Testing
dev_appserver.py app.yaml

# Production Deployment
gcloud auth login
gcloud config set project rmd2-1037
gcloud app deploy app.yaml index.yaml

# Visit Porduction Site
gcloud app browse
```