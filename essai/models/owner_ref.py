from odoo import models, fields, api

class OwnerRef(models.Model):
    _name = 'owner.ref'
    _description = 'OwnerRef'
    _order = 'id desc'

    name = fields.Char(
        string='Nom structure',
        required=True
    )
    description = fields.Char(
        string='Description'
    )