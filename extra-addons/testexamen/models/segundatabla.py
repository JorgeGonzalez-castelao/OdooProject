# -*- coding: utf-8 -*-

from odoo import fields, models

class TestModel(models.Model):
    _name = "pepita"
    _description = "muy buena pana"


    name= fields.Char(string="nombre")
    description= fields.Text(string="Descripcion")
    altura = fields.Float(string="altura")