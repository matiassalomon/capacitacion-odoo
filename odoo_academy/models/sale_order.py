# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    session_id = fields.Many2one(comodel_name='academy.session', 
                                 string='Clase relacionada',
                                ondelete='set null')

    instructor_id = fields.Many2one(string='Instructor de la clase',
                                    related='session_id.instructor_id') 
    
    students_ids = fields.Many2many(string='Estudiantes',
                                    related='session_id.students_ids')
    
    