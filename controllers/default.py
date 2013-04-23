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

  if not session.counter:
    session.counter = 1
  else:
    session.counter += 1
  return dict(form=form, latitude=latitude, longitude=longitude, 
              counter=session.counter)

def error():
  return dict()

def sites():
  rows = db().select(db.site.SiteID)
  return dict(rows=rows)  

@auth.requires_login()
@auth.requires_membership('engineer')
def logInfo():
  site = request.args(0,cast=int)
  device = db(db.device.Site == site).select() or redirect(URL('sites'))
  devicePackets = []
  for d in device:
    rows = db(db.device_log.DeviceID == d.MACAddress).select(db.device_log.ALL, orderby=db.device_log.DeviceID)
    packets = []
    for row in rows:
      vals = row.CritVals
      vals = map(int, vals.split(','))
      packets.append(vals[0])
    devicePackets.append(packets)
  return dict(rows=rows, dp=devicePackets)


