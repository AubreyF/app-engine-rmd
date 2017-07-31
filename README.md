# RobertMillerDesigner.com

* This repo includes the source code and image assets for RobertMillerDesigner.com.

# App Engine Snippets
```
# Local Testing Setup
pip install -r requirements.txt -t lib/

# Local Testing
dev_appserver.py app.yaml

# Production Deployment Setup
gcloud auth login
gcloud config set project rmd2-1037

# Production Deployment
gcloud app deploy app.yaml index.yaml

# Visit Production Site
gcloud app browse
```