# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Management(models.Model):
    
    _name = "sac.management"
    
    _description = "Gestion de SAC"

    _inherit = ['mail.thread']
    
    name = fields.Char(string="Título", required=True)

    detalle = fields.Char(string="Detalle", required=True)

    partner_id = fields.Many2one(string="Colegio", comodel_name="res.partner")

    user_id = fields.Many2one(string="Responsable", comodel_name="res.users")

    colegio_url = fields.Char(string="URL Colegio", required=True, default="http://")

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
    
    
    @api.onchange('partner_id')
    def _precargar_url(self):
        self.colegio_url = self.partner_id.name

    @api.onchange('colegio_url')
    def _format_url(self):
        if self.colegio_url and not self.colegio_url.startswith('http://') and not self.colegio_url.startswith('https://'):
            self.colegio_url = 'http://' + self.colegio_url


    @api.constrains('colegio_url')
    def _check_url(self):
        import re
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        for record in self:
            if record.colegio_url is None or not regex.search(record.colegio_url) :
                raise ValidationError('Debe ingresar una URL válida.')

