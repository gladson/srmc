#!/usr/bin/python
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/home/srmc/.local/lib/")
sys.path.insert(0, "/home/srmc/")

# Switch to the directory of your project.
os.chdir("/home/srmc/")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "srmc.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="prefork", daemonize="false")