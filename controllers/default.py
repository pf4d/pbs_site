# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

def index():
  from gluon.tools import geocode
  latitude = longtitude = ''
  form=SQLFORM.factory(Field('search'), _class='form-search')
  form.custom.widget.search['_class'] = 'input-long search-query'
  form.custom.submit['_value'] = 'Search'
  form.custom.submit['_class'] = 'btn'
  if form.accepts(request):
    address=form.vars.search
    (latitude, longitude) = geocode(address)
  else:
    (latitude, longitude) = ('','')
  return dict(form=form, latitude=latitude, longitude=longitude)

def error():
    return dict()

def myplot():
    response.headers['Content-Type']='image/png'
    return plot(data={'my plot':[(0,0),(1,1),(2,4),(3,9),(4,16)]})

def first():
    return dict()

def second():
    return dict()

def myhist():
    response.headers['Content-Type']='image/png'
    return hist()


