#coding:utf-8
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")    #projectΪ��Ŀ�����밴�����޸�
application = get_wsgi_application()