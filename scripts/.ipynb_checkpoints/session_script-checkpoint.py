from xmlrpc import client

url = 'https://matiassalomon-capacitacion-odoo-primer-modulo-2929969.dev.odoo.com'
db = 'matiassalomon-capacitacion-odoo-primer-modulo-2929969' #La base de datos es lo que aparece entre paréntesis al lado del nombre en la vista debug
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
#print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))
models_access = models.execute_kw(db, uid, password, 
                                  'academy.session', 'check_access_rights',
                                  ['write'], {'raise_exception': False})

#print(models_access)

courses  = models.execute_kw(db, uid, password, 
                                  'academy.course', 'search_read',
                                  [[['level', 'in', ['intermediate', 'beginner']]]])

#print(courses)


course = models.execute_kw(db, uid, password, 
                                  'academy.course', 'search',
                                  [[['name', '=', 'Contabilidad 200']]])

#print(course)

instructor = models.execute_kw(db, uid, password, 
                                  'res.partner', 'search',
                                  [[['name', 'ilike', 'mat']]])

#print(instructor)

session_fields = models.execute_kw(db, uid, password, 
                                  'academy.session', 'fields_get',
                                  [], {'attributes': ['string', 'type', 'required']})

#print(session_fields)

new_session = models.execute(db, uid, password,
                               'academy.session', 'create',
                                [
                                    {
                                        'course_id':course[0],
                                        'duration': 5,
                                        'instructor_id': instructor[0]
                                    }
                                ])
print(new_session)

