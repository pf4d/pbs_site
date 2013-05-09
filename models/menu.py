response.title = ('PBS Towers')
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Map'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Sites'),URL('default','sites')==URL(),URL('default','sites'),[]),
(T('Manage'),URL('default','manage')==URL(),URL('default','manage'),[])
]
