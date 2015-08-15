#!/usr/bin/env python

slideList = {'tipplewood': 3, 'willowbend': 13, 'woodrun4': 9, 'woodrun5': 6, 'sanjuan': 9, 'westlake': 5, 'beverlyhills': 0, 'color_sketches': 10, 'tortuga': 9, 'thousandoaks': 6, 'hombeyhills': 11, 'ecocity': 5, 'seattle': 0, 'sterlingchandler': 5, 'woodrun7': 5, 'snowmassclub': 8, 'casadeemdeko': 3, 'puertovallarta': 0, 'illinois': 5, 'sherekhan': 9, 'source': 0, 'kahala': 4, 'maunakea': 5, 'waterford': 13, 'indiana': 7, 'black_and_white_sketches': 10, 'wilshire': 7, 'kiddisland': 2, 'hahn': 5, 'palmsprings': 2, 'orcas': 5, 'snowmassranch': 4, 'snowmass7': 7, 'thepark': 7, 'arrowpoint': 2, 'medina': 8, 'robertrose': 8, 'woodrun': 0, 'ladera': 7, 'makanikaimarina': 4, 'napavalley': 5, 'lot8': 5, 'sandpoint': 4, 'stoneybrook': 2, 'waiikii': 3, 'lot2': 5, 'lot1': 8, 'hawaii': 6, 'exotica': 5, 'serenity': 12}

import os
import re
import logging
import pickle
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {
        }
        self.response.out.write(template.render(TemplatePath('index'), template_values))
        self.response.headers.add_header('Cache-Control', 'max-age=3600')

class NotFound(webapp.RequestHandler):
    def get(self):
        self.response.headers.add_header('Cache-Control', 'max-age=3600')
        self.redirect("/", permanent=True)
        
class SlideShow(webapp.RequestHandler):
    def get(self, title, args=""):
        
        #Init
        title = title.strip('/"\'\\');   #Disable directory traversal hacking...
        i = 0
        imgs = ""
        data = ""
        
        #Generate sequential image list
        if(args == ""):
            while i < slideList[title]:
                i += 1
                img = '%s/%d' % (title, i);
                imgs += '<img id="slide-%d" src="/img/gallery/%s.jpg" />' % (i, img)
                if(data != ""): data += ', ';
                data += "'%s.jpg'" % (img, )
                #thumbs += '<li><a href="#slide-%d"><img src="/img/gallery/%s.jpg" width="50" height="40" /></a></li>' % (i, img)
                
        #Generate custom image list
        else:
            for img in args.split('-'):
                i += 1
                img = title + "/" + img;
                imgs += '<img id="slide-%d" src="/img/gallery/%s.jpg" />' % (i, img)
                if(data != ""): data += ', ';
                data += "'%s.jpg'" % (img, )
                #thumbs += '<li><a href="#slide-%d"><img src="/img/gallery/%s.jpg" width="50" height="40" /></a></li>' % (i, img)
        
        #Generate page
        template_values = {
            'title': 'Viewing Slideshow: ' + title,
            'images': imgs,
            'data': data,
        }
        self.response.out.write(template.render(TemplatePath('slideshow'), template_values))
        self.response.headers.add_header('Cache-Control', 'max-age=3600')

def TemplatePath(name):
    return os.path.join('.', 'content', 'templates', name + '.html')

def main():
    
    #Duplicate image galleries into the static filesystem - see http://code.google.com/appengine/forum/python-forum.html?place=topic%2Fgoogle-appengine-python%2FVqfqHUvjQFU%2Fdiscussion
    global slideList
    if (os.environ['SERVER_SOFTWARE'].startswith('Development')):
        slideList = {}
        for folder in os.listdir(os.path.join('content', 'images', 'gallery')):
            slideList.setdefault(folder, 0)
            while slideList[folder] < 25:
                if(os.path.exists(os.path.join('content', 'images', 'gallery', folder, '%i.jpg' % ((slideList[folder] + 1), ) )) != True):
                    break
                slideList[folder] += 1
        #pickle.dump(slideList, open(os.path.join('cache', 'slideList'), 'w+'))
        #memcache.add("slideList", pickle.dumps(slideList))
        #logging.warn("====SlideList====" + pickle.dumps(slideList) + "====")
        logging.warn(slideList)
    #else:
        #slideList = pickle.load(open(os.path.join('cache', 'slideList'), 'r'))
        #slideList = memcache.get("slideList")
    
    application = webapp.WSGIApplication([
        ('/show/(.*)/(.*)', SlideShow),
        ('/show/(.*)', SlideShow),
        ('/', MainPage),
        ('/.*', NotFound),
        ], debug=True)
    
    util.run_wsgi_app(application)

if __name__ == '__main__':
    main()
