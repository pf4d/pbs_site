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

@auth.requires_membership('admin')
def manage():
  # web2py has a nifty smart grid for editing info from the database.
  grid = SQLFORM.smartgrid(db.auth_membership,linked_tables=['post'])
  return dict(grid=grid)

@auth.requires_login()
@auth.requires_membership('engineer')
def logInfo():
  
  # site from link clicked in default/views/sites.html link :
  site   = request.args(0,cast=int)

  # get a dict of all devices associated with the site :
  device = db(db.device.Site == site).select() or redirect(URL('sites'))

  # get a list of logs for the site ordered by date:
  logs   = db().select(db.maintenance_log.ALL, orderby=db.maintenance_log.Date)
 
  devicePackets = [] # total packets sent 
  info          = [] # current info on device
  dlist         = [] # list of device names (MAC addresses)

  # log input default values :
  db.maintenance_log.EngID.default    = auth.user_id
  db.maintenance_log.Date.default     = request.now
  db.maintenance_log.SiteID.default   = site
  db.maintenance_log.MaintenanceID.readable = False
  db.maintenance_log.MaintenanceID.writable = False
  
  # create a form for updating the maintenance log :
  form = SQLFORM(db.maintenance_log)
  if form.process().accepted:
    response.flash = 'log saved'
  
  # for each available device, give the critical values :
  for d in device:
    dlist.append(d.MACAddress)
    # get dict of all device logs ordered by deviceID
    rows = db(db.device_log.DeviceID == d.MACAddress).select(db.device_log.ALL, orderby=db.device_log.DeviceID)
    packets = []    # packets list for the current device
    first   = True  # this is the very first log
    
    # get info from each device :
    for row in rows:
      # provide only the latest batch of info :
      if first:
        info.append(row.LogInfo)
        first = False
      vals = row.CritVals
      vals = map(int, vals.split(','))
      packets.append(vals[0])
    devicePackets.append(packets)
 
  return dict(dlist=dlist, rows=rows, dp=devicePackets, 
              logs=logs, info=info, form=form)







