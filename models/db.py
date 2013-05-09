# -*- coding: utf-8 -*-
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

import dbaccess as dba
db = DAL(dba.database_uri, migrate=False)

## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate

auth = Auth(db)
# add extra fields not defined by Auth :
auth.settings.extra_fields['auth_user'] = [Field('username'), Field('phone_number')]
auth.define_tables(migrate=False, username=True)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
#auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login  = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification   = False
auth.settings.registration_requires_approval       = True
auth.settings.reset_password_requires_verification = True
auth.settings.create_user_groups                   = False

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

db.define_table('device',
    Field('MACAddress','string'),
    Field('SerialNo','string'),
    Field('UMTagNo','string'),
    Field('Make','string'),
    Field('Model','string'),
    Field('IPAddress','string'),
    Field('RoomNum','string'),
    Field('FWVer','string'),
    Field('LoginUser','string'),
    Field('LoginPW','string'),
    Field('Status','string'),
    Field('Site','integer'),
    primarykey=['MACAddress'])

#--------
db.define_table('device_log',
    Field('LogID','integer'),
    Field('DeviceID','string'),
    Field('Tag','string'),
    Field('LogInfo','text'),
    Field('LogDateTime','datetime'),
    Field('CritVals','text'),
    primarykey=['LogID'])

#--------
db.define_table('engineer_info',
    Field('Person','integer'),
    Field('SID','integer'),
    Field('ContRenewDate','date'),
    primarykey=['Person', 'SID'])

#--------
db.define_table('lease',
    Field('LeaseID','integer'),
    Field('ContractNum','string'),
    Field('RenewalDate','date'),
    Field('Contact','string'),
    Field('Phone','string'),
    Field('Address','string'),
    Field('Site','integer'),
    Field('LEASEcol','string'),
    primarykey=['LeaseID'])

#--------
db.define_table('maintenance_log',
    Field('MaintenanceID','integer'),
    Field('SiteID','integer'),
    Field('EngID','integer'),
    Field('Date','string'),
    Field('Report','string'),
    primarykey=['MaintenanceID'])

#--------
db.define_table('maintenance_log_has_device',
    Field('MaintID','integer'),
    Field('DeviceID','string'),
    primarykey=['MaintID', 'DeviceID'])

#--------
db.define_table('person',
    Field('PersonID','integer'),
    Field('Name','string'),
    Field('Email','string'),
    Field('PhoneNum','string'),
    Field('Street','string'),
    Field('City','string'),
    Field('Zip','string'),
    Field('Status','string'),
    Field('PassHash','string'),
    Field('Seed','string'),
    primarykey=['PersonID'])

#--------
db.define_table('site',
    Field('SiteID','integer'),
    Field('Name','string'),
    Field('Type','string'),
    Field('Latitude','string'),
    Field('Longitude','string'),
    Field('Elevation','string'),
    Field('Callsign','string'),
    Field('Description','string'),
    primarykey=['SiteID'])

#--------
db.define_table('site_has_utility',
    Field('Site','integer'),
    Field('Utility','integer'),
    primarykey=['Site', 'Utility'])

#--------
db.define_table('utility',
    Field('UtilityID','integer'),
    Field('Type','string'),
    Field('Name','string'),
    Field('Contact','string'),
    Field('Phone','string'),
    Field('Address','string'),
    Field('AccNum','string'),
    primarykey=['UtilityID'])

## after defining tables, uncomment below to enable auditing
auth.enable_record_versioning(db)

mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login  = settings.email_login
