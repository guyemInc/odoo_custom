from odoo import models, fields, api

class Label(models.Model):
    _name = 'label'
    _description = 'label'
    _order = 'id desc'

    name = fields.Char(
        string='Label',
        required=True
    )
    description = fields.Char(
        string='Description'
    )