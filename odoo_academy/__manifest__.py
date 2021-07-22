# -*- coding: utf-8 -*-
{
    'name': 'Odoo Academy',
    'summary': """Ejemplo de un módulo para Odoo""",
    'description': """
        Ejemplo de un módulo para Odoo en Phyton que permitirá:
            - Probar si puedo agregar módulos a Odoo.
            - Extender funcionalidad sobre módulos existentes.
            - Probar mis conocimientos.
    """,
    'author': 'Matías Salomón',
    'website': 'https://kdoce.cl',
    'category': 'Training',
    'version': '0.1',
    'depends': ['sale_management','website'],
    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
        'views/sale_views_inherit.xml',
        'views/product_views_inherit.xml',
        'wizard/sale_wizard_view.xml',
        'report/session_report_templates.xml',
        'views/academy_web_templates.xml'
    ],
    'demo': [
        'demo/academy_demo.xml',
    ]
}
