import xmlrpclib

db = "prod_desa"
username = "joelunmsm@gmail.com"
password = "rosa0000"
url = "http://174.138.77.53:8069"

common =xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
# common.version()
# print common
uid =common.authenticate(db, username, password,{})

# name =raw_input("Introduce en nombre")
# celular =raw_input("Introduce el celular")
# departamento =raw_input("Introduce el departamento")
# email =raw_input("Introduce el email")
# telefono =raw_input("Introduce el telefono")

models =xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
# id = models.execute_kw(db, uid, password, "hr.employee", "create",[{


# 	"name":name,
# 	"mobile_phone":celular,
# 	"work_location":departamento,
# 	"work_email":email,
# 	"work_phone":telefono,

# }] )


models.execute_kw(db, uid, password,
    'hr.employee', 'search',
    [[['name', '=', 'exitos;)']]])


models.execute_kw(
    db, uid, password, 'hr.employee', 'fields_get',
    [], {'attributes': ['string', 'help', 'type']})


print models.execute_kw(db, uid, password,
    'hr.employee', 'search_read',
    [[['name', '=', 'exitos;)']]],
    {'fields': ['name','comment'], 'limit': 5})
