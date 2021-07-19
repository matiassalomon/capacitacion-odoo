# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

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
    
    base_price = fields.Float(string="Precio base", default=0.00)
    
    additional_fee = fields.Float(string="Tasa adicional", default=0.00)
    
    total_price = fields.Float(string="Precio total", readonly=True)
    
    sessions_ids = fields.One2many(comodel_name='academy.session',
                                  inverse_name='course_id',
                                  string='Clases')
    
    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        
        if self.base_price < 0.00:
            raise UserError('El precio base no puede ser negativo.')
        
        self.total_price = self.base_price + self.additional_fee
        
    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError('La tasa adicional no puede ser menor a $10.00: %s ' % record.additional_fee)
    
    
                
        
    