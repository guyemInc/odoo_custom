from odoo import models, fields

class ImmeubleState(models.Model):
    _name = 'immeuble.state'
    _description = 'Statut'
    _order = 'id desc'

    name = fields.Char(
        string='Statut',
        required=True
    )
    description = fields.Char(
        string='Description',
        required=True
    )