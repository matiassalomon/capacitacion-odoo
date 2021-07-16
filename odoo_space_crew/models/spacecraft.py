# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Spacecraft(models.Model):
    
    _name = "spacecrew.spacecraft"
    
    _description = "Datos de una nave espacial."
    
    nombre = fields.Char(string="Nombre", help="Nombre de la nave espacial")
    
    tipo = fields.Selection(string="Tipo de nave espacial",
                                   selection=[
                                       ('tourist', 'Nave espacial turística'),
                                       ('moon', 'Nave espacial lunar'),
                                       ('intergalactic', 'Nave espacial intergaláctica'),
                                       ('timetraveler', 'Nave espacial que puede viajar en el tiempo')
                                   ]
                                  )
    
    combustible = fields.Selection(string="Tipo de combustible",
                                   selection=[
                                       ('bencina-95', 'Nafta Súper'),
                                       ('bencina-98', 'Nafta Premium'),
                                       ('diesel', 'Gasoil'),
                                       ('kerosene', 'Kerosene para cohetes'),
                                       ('nuclear', 'Combustible nuclear')
                                   ]
                                  )
    
    foto = fields.Image(string="Imagen", help="Imagen de la nave espacial.", required=False)
    
    capacidad = fields.Integer(string="Capacidad de pasajeros", required=True)
    
    peso = fields.Integer(string="Peso", required=True, help="Peso en kilos de la nave.")
    
    alto = fields.Float(string="Alto", required=True, help="Alto en metros de la nave, puede contener decimales.")
    
    active = fields.Boolean(string="Activo", default=True)
    
    detalle = fields.Text(string="Detalles", help="Detalles extras de la nave espacial.")