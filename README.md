pbs_site
========

PBS radio tower status website

To install:
-----------
**Linux and Unix**

One step production deployment
Here are some steps to install apache+python+mod_wsgi+web2py+postgresql from scratch.

On Ubuntu:
```bash
wget http://web2py.googlecode.com/hg/scripts/setup-web2py-ubuntu.sh 
chmod +x setup-web2py-ubuntu.sh
sudo ./setup-web2py-ubuntu.sh
```

On Fedora:
```bash
wget http://web2py.googlecode.com/hg/scripts/setup-web2py-fedora.sh
chmod +x setup-web2py-fedora.sh
sudo ./setup-web2py-fedora.sh
```

Both of these scripts should run out of the box, but every Linux installation is a bit different, so make sure you check the source code of these scripts before you run them. In the case of Ubuntu, most of what they do is explained in the link below.

Once this is installed, you can go to https://localhost, click "admin interface" and then "Upload and install packed application."  You can copy the git address above (https://github.com/pf4d/pbs_site) to the "Or get from URL" box and install.

Full documentation on deployment found here:
http://web2py.com/books/default/chapter/29/13

Google Maps
-----------

The script used to display googlemaps is called gmaps.js and is located in the static/js directory.  A detailed explanation of its usage is found at http://hpneo.github.com/gmaps/
