from xmlrpc import client

url = 'https://matiassalomon-capacitacion-odoo-primer-modulo-2929969.dev.odoo.com'
db = 'matiassalomon-capacitacion-odoo-primer-modulo-2929969' #La base de datos es lo que aparece entre paréntesis al lado del nombre en la vista debug
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))
models_access = models.execute_kw(db, uid, password, 
                                  'sale.order', 'check_access_rights',
                                  ['write'], {'raise_exception': False})

print(models_access)

draf_quotes = models.execute_kw(db, uid, password, 
                                  'sale.order', 'search',
                                  [[['state', '=', 'draft']]])
print(draf_quotes)

if_confirmed = models.execute_kw(db, uid, password, 
                                  'sale.order', 'action_confirm',
                                  [draf_quotes])

print(if_confirmed)