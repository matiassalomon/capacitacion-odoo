# -*- coding: utf-8 -*-
{
    'name': 'Odoo Space Crew',
    'summary': """Registro de datos de naves espaciales""",
    'description': """
        El módulo permite llevar un control de:
            - Naves espaciales con sus respectivos datos.
    """,
    'author': 'Matías Salomón',
    'website': 'https://kdoce.cl',
    'category': 'Training',
    'version': '0.1',
    'depends': ['web'],
    'data': [
        'security/space_crew_security.xml',
        'security/ir.model.access.csv',
        'views/space_crew_menuitems.xml',
        'views/spacecrew_views.xml',
        'views/css_loader.xml',
    ],
    'demo': [
        'demo/spacecraft.xml',
    ]
}