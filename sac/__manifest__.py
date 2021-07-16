# -*- coding: utf-8 -*-
{
    'name': 'Gestión de llamados, correos y chats a SAC',
    'summary': "Gestión de los llamados, correos y chats recibidos por el equipo de SAC",
    'description': """
        El objetivo de este módulo es permitir el registro de las solicitudes de contacto que recibe el equipo de SAC
        Actual:
            - Registrar las solicitudes de conectato.
        Futuro:
            - Generar reportes de estas gestiones.

    """,
    'author': 'Matías Salomón',
    'website': 'https://kdoce.cl',
    'version': '0.2',
    'depends': ['mail'],
    'data': [
        'security/management_security.xml',
        'security/ir.model.access.csv',
	    'views/management_views.xml',
        'views/management_menuitems.xml'
    ],
    'demo': [

    ]
}