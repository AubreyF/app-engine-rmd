#!/usr/bin/env python
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

import webapp2

import django
from django.template.loader import render_to_string

django.setup()

SLIDE_LIST = {
    'arrowpoint': 9,
    'beverlyhills': 0,
    'black_and_white_sketches': 10,
    'burnett': 4,
    'casadeemdeko': 3,
    'color_sketches': 10,
    'ecocity': 5,
    'exotica': 5,
    'hahn': 5,
    'hawaii': 6,
    'hombeyhills': 11,
    'illinois': 5,
    'indiana': 7,
    'kahala': 4,
    'kiddisland': 2,
    'ladera': 7,
    'lot1': 8,
    'lot2': 5,
    'lot8': 5,
    'makanikaimarina': 4,
    'maunakea': 5,
    'medina': 8,
    'napavalley': 8,
    'nineoneone': 11,
    'orcas': 5,
    'palmsprings': 2,
    'puertovallarta': 0,
    'quailcrossing': 3,
    'robertrose': 8,
    'sandpoint': 4,
    'sanfranpent': 14,
    'sanjuan': 9,
    'sarasota': 2,
    'seattle': 0,
    'sellekhawaii': 1,
    'serenity': 26,
    'sherekhan': 9,
    'snowmass7': 6,
    'snowmassclub': 8,
    'snowmassranch': 5,
    'source': 0,
    'sterlingchandler': 5,
    'stoneybrook': 7,
    'tacoma': 5,
    'tahoe': 13,
    'thepark': 7,
    'thousandoaks': 6,
    'tipplewood': 10,
    'tortuga': 9,
    'turnpointcove': 6,
    'waterford': 18,
    'waiikii': 3,
    'westlake': 5,
    'willowbend': 13,
    'wilshire': 7,
    'woodrun': 0,
    'woodrun4': 9,
    'woodrun5': 6,
    'woodrun7': 5,
}


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'cache_buster': '?v=' + os.environ['CURRENT_VERSION_ID'],
        }
        self.response.out.write(render_to_string('index.html', template_values))
        self.response.headers.add_header('Cache-Control', 'max-age=3600')


class NotFound(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header('Cache-Control', 'max-age=3600')
        self.redirect("/", permanent=True)


class SlideShow(webapp2.RequestHandler):
    def get(self, title="", images=""):

        # Init
        title = title.strip('/"\'\\');  # Disable directory traversal hacking...
        i = 0
        imgs = ""
        data = ""

        # Generate sequential image list
        if images == "":
            while i < SLIDE_LIST[title]:
                i += 1
                img = '%s/%d' % (title, i)
                imgs += ('<img id="slide-%d" src="/img/gallery/%s.jpg?v=' + os.environ['CURRENT_VERSION_ID'] + '" />') % (i, img)
                if (data != ""): data += ', '
                data += ("'%s.jpg?v=" + os.environ['CURRENT_VERSION_ID'] + "'") % (img,)
                # thumbs += '<li><a href="#slide-%d"><img src="/img/gallery/%s.jpg" width="50" height="40" /></a></li>' % (i, img)

        else:
            # Generate custom image list
            for img in images.split('-'):
                i += 1
                img = title + "/" + img
                imgs += ('<img id="slide-%d" src="/img/gallery/%s.jpg?v=' + os.environ['CURRENT_VERSION_ID'] + '" />') % (i, img)
                if data != "": data += ', '
                data += ("'%s.jpg?v=" + os.environ['CURRENT_VERSION_ID'] + "'") % (img,)
                # thumbs += '<li><a href="#slide-%d"><img src="/img/gallery/%s.jpg" width="50" height="40" /></a></li>' % (i, img)

        # Generate page
        template_values = {
            'title': 'Viewing Slideshow: ' + title,
            'images': imgs,
            'data': data,
        }
        self.response.out.write(render_to_string('slideshow.html', template_values))
        self.response.headers.add_header('Cache-Control', 'max-age=3600')


app = webapp2.WSGIApplication([
    ('/show/(.*)/(.*)', SlideShow),
    ('/show/(.*)', SlideShow),
    ('/', MainPage),
    ('/.*', NotFound),
], debug=True)
