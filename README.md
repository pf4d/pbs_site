pbs_site
========

PBS radio tower status website
!
To install web2py and pbs_site:
-------------------------------
**Linux and Unix**

Here is a good explanation of how to install web2py:
http://jdoe.asidev.com/2009/02/26/configure-web2py-to-run-behind-apache-with-wsgi-mod_wsgi/


I was not able to install pbs_site by providing the git URL, but have installed it successfully as follows:  First, clone the repository into a temp directory, then tar the files like so:
```bash
cd temp_dir/pbs_site
tar zcvf web2py.app.name.w2p *
```
Then install the "packed" application in the web2py admin interface.  Afther this, remove the directory ```applications/pbs_site``` and copy the ```pbs_site``` directory from ```temp_dir``` into the ```applications``` directory where you just deleted the ```pbs_site``` folder.  You will now be able to perform all the necessary commits and such that you need.


One step production deployment
------------------------------
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

File descriptions
-----------------

The only files which you should need to change (and also that I have changed) are described below.  I have included commenting in these files to further guide your designs.


* ```pbs_site/controllers/default.py``` -- the main controller page with all the actions needed to display the views described below.
* ```pbs_site/views/default/error.html``` -- error html view.
* ```pbs_site/views/default/index.html``` -- main map view.
* ```pbs_site/views/default/logInfo.html``` -- graphs and stats for site.
* ```pbs_site/views/default/sites.html``` -- page to select a site to view log info.
* ```pbs_site/views/default/manage.html``` -- admin database management page.
* ```pbs_site/models/0.py``` -- database variables used by the admin interface.
* ```pbs_site/models/db.py``` -- database definition and parameters.
* ```pbs_site/models/menu.py``` -- top-level menu items.
* ```pbs_site/static/css/web2py.css``` -- css for all elements of the site.
* ```pbs_site/modules/dbaccess.py``` -- secret file for connecting to database and setting up email.
* ```pbs_site/scripts/extract_mysql_models.py``` -- script for connecting to database and providing web2py database definitions for ```db.py```.

![screenshot](https://raw.github.com/pf4d/pbs_site/master/doc/images/pbs_site.png)
