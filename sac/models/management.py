# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Management(models.Model):
    
    _name = "sac.management"
    
    _description = "Gestion de SAC"

    _inherit = ['mail.thread']
    
    name = fields.Char(string="Título", required=True)

    detalle = fields.Char(string="Detalle", required=True)

    partner_id = fields.Many2one(string="Colegio", comodel_name="res.partner")

    user_id = fields.Many2one(string="Responsable", comodel_name="res.users")

    url = fields.Char(string="URL Colegio", required=True)

    active = fields.Boolean(string="Activo", default=True)

    servicio = fields.Selection(string="Servicio",
                                 selection=[
                                            ('LLE', 'LLE'),
                                            ('masterclass', 'MasterClass'),
                                            ('videoclass', 'VideoClass'),
                                            ('laboratorio', 'Laboratorio')
                                            ],
                                default="masterclass"
                             )

    estado = fields.Selection(string="Estado",
                                 selection=[
                                            ('recibido', 'Recibido'),
                                            ('proceso', 'En Proceso'),
                                            ('desarrollo', 'Derivado a Desarrollo'),
                                            ('contenido', 'Derivado a Contenido'),
                                            ('resuelto', 'Resuelto'),
                                            ('rechazado', 'Rechazado')
                                            ],
                                default="recibido"
                             )

    tipo = fields.Selection(string="Tipo",
                              selection=[
                                  ('consulta', 'Consulta'),
                                  ('procedimiento', 'Solicitud de procedimiento'),
                                  ('usuario', 'Capacitacion a Usuario'),
                                  ('sistema', 'Falla de Sistema'),
                                  ('contenido', 'Cambios en Contenido')
                                ],
                                default="consulta"
                              )

    entrada = fields.Selection(string="Forma de contacto",
                              selection=[
                                  ('tel', 'Telefono'),
                                  ('email', 'Correo electronico'),
                                  ('chat', 'Chat')
                                ],
                                default="tel"
                              )

    contacto_nommbre = fields.Char(string="Contacto", required=True)
    
    contacto_tel = fields.Char(string="Teléfono", required=False)
    
    contacto_email = fields.Char(string="E-Mail", required=False)
