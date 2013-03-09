response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('myplot'),URL('default','myplot')==URL(),URL('default','myplot'),[]),
(T('myhist'),URL('default','myhist')==URL(),URL('default','myhist'),[]),
(T('first'),URL('default','first')==URL(),URL('default','first'),[]),
]
