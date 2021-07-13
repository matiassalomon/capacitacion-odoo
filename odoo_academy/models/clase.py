# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Clase(models.Model):
    _name = "academy.course.clase"
    _description = "Detalles de una clase"
    
    name = fields.Char(string="Clase", help="Nombre de la clase", required=True)
    duracion = fields.Integer(string="Duración", help="Duración de la clase en minutos", required=True, default=45)
    contenido = fields.Text(string="Contenido", help="Contenido de la clase")
    teoria = fields.Binary(string="PDF Teoría", help="Archivo PDF con la teoría de la clase", required=True)
    practica = fields.Binary(string="PDF Práctica", help="Archivo PDF con los ejercicios prácticos de la clase", required=False)
    
    