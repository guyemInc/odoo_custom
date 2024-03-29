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
    owner_ref_id = fields.Many2one('owner.ref',
        string='Editeur Label', 
        ondelete='restrict'
        )
    label_version_ids = fields.One2many('label.version',
         'label_id',
        string='Versions'
        )
    