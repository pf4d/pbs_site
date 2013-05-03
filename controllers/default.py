# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
'''
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
'''
def error():
  return dict()

def sites():
  rows = db().select(db.site.SiteID)
  return dict(rows=rows)  

@auth.requires_membership('admin')
def manage():
  grid = SQLFORM.smartgrid(db.auth_membership,linked_tables=['post'])
  return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('engineer')
def logInfo():
  site   = request.args(0,cast=int)
  device = db(db.device.Site == site).select() or redirect(URL('sites'))
  devicePackets = []
  info   = []
  dlist  = []
  # for each available device, give the critical values :
  for d in device:
    dlist.append(d.MACAddress)
    rows = db(db.device_log.DeviceID == d.MACAddress).select(db.device_log.ALL, orderby=db.device_log.DeviceID)
    packets = []
    first = True
    for row in rows:
      # provide the latest batch of info :
      if first:
        info.append(row.LogInfo)
        first = False
      vals = row.CritVals
      vals = map(int, vals.split(','))
      packets.append(vals[0])
    devicePackets.append(packets)
  return dict(dlist=dlist, rows=rows, dp=devicePackets, info=info)

def index():
    raw_err = db.executesql('SELECT DISTINCT Site FROM device_log JOIN device ON device.MACAddress = device_log.DeviceID'
        + ' WHERE LogDateTime >= SYSDATE() - INTERVAL 1 DAY AND Tag = "ERROR";')
    err = []
    for i in raw_err:
      err.append(int(i[0]))
    rows = db(db.site).select()
    lats = []
    lngs = []
    site = []
    name = []
    baseInt = 0
    erLat = []
    erLng = []
    erSite = []
    erName = []
    erNum = 0
    workingNum = 0
    for row in rows:
      if row.SiteID in err:
        erLat.append(row.Latitude)
        erLng.append(row.Longitude)
        erSite.append(row.SiteID)
        erName.append(row.Name)
        erNum = erNum+1
      else:
        lats.append(row.Latitude)
        lngs.append(row.Longitude)
        site.append(row.SiteID)
        name.append(row.Name)
        workingNum = workingNum+1

    return dict(lats=lats,lngs=lngs,site=site,name=name,err=err,baseInt=baseInt,erLat=erLat,erLng=erLng,erSite=erSite,erName=erName,
                workingNum=workingNum,erNum=erNum)
                                                                                                                              98,1          Bot

