# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_session_product = fields.Boolean(string="Considerar como una clase",
                                       help="Tildar para usar este  producto para la tasa de una clase",
                                       default=False)
    
    
    
