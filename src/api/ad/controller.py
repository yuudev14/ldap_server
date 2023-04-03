from fastapi import Request, APIRouter, Path
from fastapi_utils.cbv import cbv
import ldap3


from src.config.ldap_connection import ldap_conn
import src.constants as constants

ad_route = APIRouter()


@cbv(ad_route)
class AuthController:
    
    # def __init__(self):
    #     self.manager = ADManager()

    @ad_route.get("/user/{user_cn}")
    async def search_user(self, user_cn:str = Path(..., description="user should exist")):
        # extract search parameters from the request
        
        ldap_conn.bind()

        base_dn = f"ou=users,{constants.LDAP_BASE_DN}"
        search_filter = '(cn=*)'
        attributes = ["*"]

        ldap_conn.search(base_dn, search_filter, attributes=attributes)
        return ldap_conn.response

    @ad_route.get("/groups/members/{group}")
    async def search_group_members(self, group:str = Path(..., description="group should exist")):
        # extract search parameters from the request
        
        ldap_conn.bind()

        base_dn = f"cn={group},ou=groups,{constants.LDAP_BASE_DN}"
        search_filter = '(objectClass=*)'
        attributes = ["member"]

        ldap_conn.search(base_dn, search_filter, attributes=attributes, search_scope=ldap3.SUBTREE)
        member_emails = []
        for member_dn in ldap_conn.entries[0].member.values:
            member_filter = '(cn=*)'
            member_attributes = ['mail', 'givenName', 'cn']
            ldap_conn.search(member_dn, member_filter, attributes=member_attributes)
            member_emails.extend([{"mail": entry.mail.values[0], "givenName": entry.givenName.values[0]} for entry in ldap_conn.entries])
        ldap_conn.unbind()
        return member_emails