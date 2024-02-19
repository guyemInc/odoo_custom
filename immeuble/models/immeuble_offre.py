from random import  randint
from odoo import models, fields, api
# # syntaxe lors du cours ? provoque nonn pas Erreur, mais info syntaxe nok
# from odoo import models, fields, api, _
# from odoo.exceptions import ValidationError

class ImmeubleOffre(models.Model):
    # _inherit = 'immeuble'         # non pas d'hetirage dans ce cas passer par relation
    _name = 'immeuble.offre'
    _description = 'Offre'
    
    # def _get_default_number(self) :
    #     return randint(1,11)
    
    name = fields.Char(
        string='Nom de l\'offre'
    )
    
    immeuble_id = fields.Many2one(
        'immeuble',
        string='Immeuble'
        
    )

    offreur_id = fields.Many2one(
        'res.partner',
        string='Offreur',
        required=True
    )
    owner_id = fields.Many2one(
        'res.partner',
        string='Proprietaire',
        related='immeuble_id.owner_id'  # C'est ici la relation avec immeuble
    )
    offre_value = fields.Float(
        string='Prix proposé',
        default=0.0,
        required=False
    )
    # company_currency_id = fields.Many2one('res.currency',string="devise")

 

    @api.onchange('offreur_id','immeuble_id','offre_value')
    def _onchange_offreur_id(self):
        if self.offreur_id and self.immeuble_id :
            # self.name = 'Une offre de '+self.offreur_id.name+ ' pour ' + self.immeuble_id.name + ' pour un montant de : '+str(self.offre_value)
            self.name = 'Une offre de '+self.offreur_id.name+ ' pour ' + self.immeuble_id.name + ' pour un montant de : '
        else :
            self.name = 'En attente offre'

    # @api.constrains('offreur_id','owner_id')
    # def _check_offreur_diff_owner_id(self):
    #     if self.offreur_id == self.owner_id:
    #         raise ValidationError(_('L offre ne peut pas etre émise par le propriétaire !.'))
