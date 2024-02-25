from odoo import models, fields

class Profil(models.Model):
    _name = 'profil'
    _description = 'profil'
    _order = 'id desc'

    name = fields.Char(
        string='Profil',
        required=True
    )
    description = fields.Char(
        string='Description'
    )