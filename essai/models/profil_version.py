from odoo import models, fields

class ProfilVersion(models.Model):
    _name = 'profil.version'
    _description = 'profil version'
    _order = 'id desc'

    profil_id = fields.Many2one('profil', 
        ondelete='cascade',        
        onupdate='cascade' 
    )
    name = fields.Char(
        string='Nom',
        required=True
    )
    description = fields.Char(
        string='Description'
    )
    code = fields.Char(
        string='Code',
        required=True
    )
    date_start = fields.Date(
        string='Date application'
    )
    date_end = fields.Date(
        string='Date clôture'
    )

    profil_version_repository_ids = fields.Many2many('repository.version',
        #'repository_version_id',
        string='Référentiels compatibles'
    )

