from odoo import models, fields

class Infrastructure(models.Model):
    _name = 'infrastructure'
    _description = 'infrastructure'
    _order = 'id desc'

    name = fields.Char(
        string='Nom de l\'infrastructure',
        required=True
    )