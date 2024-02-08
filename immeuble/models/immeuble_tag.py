from random import  randint
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ImmeubleTag(models.Model):
    _name = 'immeuble.tag'
    _description = 'Tag Name'
    # _parent_store = True
    # _parent_name = 'parent_id'
    _sql_constraints = [
        ('name_uniq', 'unique (name)', "Tag name already exists !")
    ]

    def _get_default_number(self) :
        return randint(1,11)
    
    # @api.constraints('parent_id')
    @api.constrains('parent_id')
    def _check_parent_id(self):
        if not self._check_recursion():
            raise ValidationError(_('You can not create recursive tags.'))

    name = fields.Char(
        string='Tag name',
        required=True
    )
    description = fields.Char(
        string='Description',
        required=True
    )

    parent_id = fields.Many2one('immeuble.tag', 
        index=True, 
        ondelete='cascade', 
        # readonly=True, 
        # hors sujet  pas de lien vers Company ici
        #   check_company=True
    )

    color = fields.Integer(
        string='Color Index',
        # default=2
        default=_get_default_number
    )
