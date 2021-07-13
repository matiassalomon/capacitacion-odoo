# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = "academy.course"
    _description = "Información del Curso"
    
    name = fields.Char(string="Título", required=True)
    
    description = fields.Char(string="Descripción", required=False)
    
    level = fields.Selection(string="Nivel",
                            selection=[('begginer', 'Principante'),
                                      ('intermediate','Intermedio'),
                                      ('advance','Avanzado')],
                             copy=False)
    
    active = fields.Boolean(string="Activo", default=True)
    
    