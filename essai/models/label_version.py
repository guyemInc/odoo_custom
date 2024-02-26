from odoo import models, fields

class LabelVersion(models.Model):
    _name = 'label.version'
    _description = 'label version'
    _order = 'id desc'

    label_id = fields.Many2one('label', 
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

    label_version_repository_ids = fields.Many2many('repository.version',
        'repository_version_id',
        string='Référentiels compatibles'
    )
    