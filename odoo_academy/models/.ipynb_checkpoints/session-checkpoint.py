# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError

class Session(models.Model):
    _name = 'academy.session'
    _description = 'Información de la clase'
    
    course_id = fields.Many2one(comodel_name='academy.course',
                               string='Curso',
                               ondelete='cascade',
                               required=True)
    
    name = fields.Char(string="Título", related='course_id.name')
    
    instructor_id = fields.Many2one(comodel_name='res.partner',
                                   string='Instructor',
                                   required=True)
    
    students_ids = fields.Many2many(comodel_name='res.partner',
                                   string='Estudiantes')
    
    start_date = fields.Date(string="Fecha de inicio",
                           default=fields.Date.today)
    
    
    duration = fields.Integer(string="Días de clases",
                           default=1)
    
    end_date = fields.Date(string="Fecha de término",
                            compute='_compute_end_date',
                            inverse='_inverse_end_date',
                            store=True)
    
    total_price = fields.Float(string='Precio total',
                              related='course_id.total_price')
    
    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date +  duration
    
    @api.depends('end_date')
    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration = (record.end_date - record.start_date).days + 1
            else:
                continue
            
            