from dotenv import load_dotenv
import os

load_dotenv()

LDAP_URL = os.getenv("LDAP_URL")
LDAP_USER = os.getenv("LDAP_USER")
LDAP_PASSWORD = os.getenv("LDAP_PASSWORD")

LDAP_BASE_DN = os.getenv("LDAP_BASE_DN")
