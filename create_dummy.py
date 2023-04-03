import ldap3

server = ldap3.Server('ldap://localhost:10389')
username = 'uid=admin,ou=system'
password = 'secret'

conn = ldap3.Connection(server, user=username, password=password)
conn.bind()

# Define the user and group entries
user1_entry = {
    'objectClass': ['top', 'person', 'inetOrgPerson'],
    'cn': 'user1',
    'sn': 'User1',
    'givenName': 'Test',
    'mail': 'user1@my-domain.com',
    'userPassword': 'password'
}
user2_entry = {
    'objectClass': ['top', 'person', 'inetOrgPerson'],
    'cn': 'user2',
    'sn': 'User2',
    'givenName': 'Test',
    'mail': 'user2@my-domain.com',
    'userPassword': 'password'
}
group1_entry = {
    'objectClass': ['top', 'groupOfNames'],
    'cn': 'group1',
    'member': [
        'cn=user1,ou=users,dc=example,dc=com',
        'cn=user2,ou=users,dc=example,dc=com'
    ]
}
ou_entry = {'objectClass': ['top', 'organizationalUnit'], 'ou': ['users']}
conn.add('ou=users,dc=example,dc=com', attributes=ou_entry)
ou_entry = {'objectClass': ['top', 'organizationalUnit'], 'ou': ['groups']}
conn.add('ou=groups,dc=example,dc=com', attributes=ou_entry)
# Add the user and group entries
conn.add('cn=user1,ou=users,dc=example,dc=com', attributes=user1_entry)
print(conn.last_error)
conn.add('cn=user2,ou=users,dc=example,dc=com', attributes=user2_entry)
print(conn.last_error)
conn.add('cn=group1,ou=groups,dc=example,dc=com', attributes=group1_entry)
print(conn.last_error)

conn.unbind()