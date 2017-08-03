# RobertMillerDesigner.com

* This repo contains the source code and image assets for RobertMillerDesigner.com.

# Adding a new slideshow gallery

1. Copy image files to new folder (with lowercase name) under /content/images/gallery. 
2. Add new entry to main.py SLIDE_LIST. Name should match folder name, number should be number of images in folder.
3. Test locally
4. Deploy
5. Test in Production

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
gcloud app deploy app.yaml index.yaml --project rmd2-1037

# Visit Production Site
gcloud app browse
```