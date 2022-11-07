import sys
from pathlib import Path
from pyad import adsearch, pyad
from os import path
import configparser
import pythoncom


DEBUG = False

Version = "v1.0.1.2"
Title = "Horizon Account Verifier"

if not DEBUG:
    exe_dir = str(path.dirname(sys.executable))
    settings_file = "Settings.ini"
else:
    exe_dir = str(Path(__file__).parents[0])
    settings_file = "Settings-debug.ini"

settings_dir = ''.join([exe_dir, '\\Settings\\'])

def getSettings(self, section):
    self.parser = configparser.RawConfigParser(
        comment_prefixes=('#', ';', '###'))
    self.parser.read(settings_dir + settings_file)

    if self.parser.has_section(section):
        # ===================SERVER================================
        if self.parser.has_option(section, 'company'):
            self.company = self.parser.get(section, 'company')[
                1:self.parser.get(section, 'company').__len__()-1]

def getConfig(self, section):
    self.parser = configparser.RawConfigParser(
        comment_prefixes=('#', ';', '###'))
    self.parser.read(settings_dir + settings_file)

    if self.parser.has_section(section):
        # ===================SERVER================================
        if self.parser.has_option(section, 'server'):
            self.server = self.parser.get(section, 'server')[
                1:self.parser.get(section, 'server').__len__()-1]
            print(self.server)
            if not self.server.__len__() <= 3:
                self.compFail = False
            else:
                self.compFail = True
                return
        # ===================SERVER USERNAME================================
        if self.parser.has_option(section, 'server_user'):
            self.username = self.parser.get(section, 'server_user')[
                1:self.parser.get(section, 'server_user').__len__()-1]
            if not self.username.__len__() <= 3:
                self.compFail = False
            else:
                self.compFail = True
                return
        # ===================SERVER PASSWORD================================
        if self.parser.has_option(section, 'server_pass'):
            self.password = self.parser.get(section, 'server_pass')[
                1:self.parser.get(section, 'server_pass').__len__()-1]
            if not self.password.__len__() <= 3:
                self.compFail = False
            else:
                self.compFail = True
                return
        # ===================USEROU================================
        if self.parser.has_option(section, 'userOU'):
            self.ou = self.parser.get(section, 'userOU')[
                1:self.parser.get(section, 'userOU').__len__()-1]
            if not self.ou.__len__() <= 3:
                self.compFail = False
            else:
                self.compFail = True
                return
        # ===================DOMAIN NAME================================
        if self.parser.has_option(section, 'domainName'):
            self.domainName = self.parser.get(section, 'domainName')[
                1:self.parser.get(section, 'domainName').__len__()-1]
            if self.domainName.__len__() <= 3:
                self.compFail = False
        else:
            self.compFail = True


def findUser(self, displayname):
    pythoncom.CoInitialize()
    pyad.set_defaults(ldap_server=self.server,
                      username=self.username, password=self.password, ssl=True)
    q = adsearch.ADQuery()
    q.execute_query(attributes=["displayName", "userPrincipalName", "sAMAccountName", "title"],
                    where_clause="objectClass = 'user' and name = '*"+displayname+"*'", base_dn=self.ou)
    users = {}
    for x in q.get_results():
        users[x['sAMAccountName']] = {
            'name': x['displayName'], 'email': x['userPrincipalName'], 'title': x['title']}
    return (users)
