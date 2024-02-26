from odoo import models, fields

class RepositoryVersion(models.Model):
    _name = 'repository.version'
    _description = 'repository version'
    _order = 'id desc'

    repository_id = fields.Many2one('repository', 
        ondelete='cascade',        
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

    profil_version_partners_ids = fields.Many2many('profil.version',
        # 'profil_version_id',
        string='Profils associés',
        required=False
    )
    
    label_version_partners_ids = fields.Many2many('label.version',
        'label_version_id',
        string='Labels associés',
        required=False
    )