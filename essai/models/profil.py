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
    owner_ref_id = fields.Many2one('owner.ref',
        string='Editeur Profil', 
        ondelete='restrict')
    
    # profil_version_ids = fields.One2many('profil.version',
    #      'profil_id',
    #     string='Versions',
    #     required=False
    #     )