# -*- coding: utf-8 -*-

from odoo import fields, models

class TestModel(models.Model):
    _name = "pepito"
    _description = "muy buen pana"


    name= fields.Char(string="nombre")
    description= fields.Text(string="Descripcion")
    edad = fields.Integer(string="15")