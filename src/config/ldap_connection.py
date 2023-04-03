import ldap3

import src.constants as constants

server = ldap3.Server(constants.LDAP_URL)
ldap_conn = ldap3.Connection(server, user=constants.LDAP_USER, password=constants.LDAP_PASSWORD)