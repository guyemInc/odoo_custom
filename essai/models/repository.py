from odoo import models, fields, api

class Repository(models.Model):
    _name = 'repository'
    _description = 'repository'
    _order = 'id desc'

    name = fields.Char(
        string='Référentiel',
        required=True
    )
    description = fields.Char(
        string='Description'
    )
    owner_ref_id = fields.Many2one('owner.ref',
        string='Editeur Label', 
        ondelete='restrict'
        )
    label_id = fields.Many2one('label',
        string='Label associé', 
        ondelete='restrict'
        )
    repository_version_ids = fields.One2many('repository.version',
         'repository_id',
        string='Versions'
        )
    