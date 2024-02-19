from odoo import models, api, fields, _
from odoo.exceptions import ValidationError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    # _name = 'Proprietaire'
    # _description = 'proprietaire'
    # _order = 'id desc'

    description_test = fields.Char(
        string='Description Custom',
        required=False
    )

    immeuble_ids = fields.One2many('immeuble', 'owner_id',  string='Proprietaire')
    # immeuble_ids = fields.One2many(
    #     'immeuble', 
    #     # 'inverse_field_name', 
    #     # compute='_compute_account_root'
    #     string='Proprietaire',
    #     required=False
    # )

    count_toto = fields.Integer(
        string='Somme des montants',        
        compute = '_compute_count_toto',
        store=True   
    )

    @api.depends('immeuble_ids')
    def _compute_count_toto(self):
        for record in self:
            #record.count_toto = len(record.immeuble_ids.filtered(lambda r : r.name == 'toto'))
            #record.count_toto = sum(record.building_value)
            #record.count_toto = sum(record.immeuble_ids.building_value)
            # ci-dessus => ValueError: Expected singleton: immeuble(14, 11, 10, 9)
            #record.count_toto = len(record.immeuble_ids)
            #record.name = record.name + " Total : " + str(record.count_toto)

            # i = 0
            # for imm in record.immeuble_ids:
            #     i = i = imm.building_value
            # record.count_toto = i
            # record.name = record.name + " Total : " + str(record.count_toto)

            record.count_toto = sum(record.immeuble_ids.mapped('building_value'))
            record.email = " Total : " + str(record.count_toto)

        #import pdb; pdb.set_trace()

    def write(self,vals):
        # Appel des méthodes de la class supérieur ()
        #       en d'autre terme appel des méthodes permettant d'écrire en bdd
        ###res = super(ResPartner, self).write(vals)
        # # tentative effacement TAG.. sans doute mieux dans un event onload res_partner
        # if len(self.immeuble_ids) == 0 :
        #     vals.update({'category_id' :
        #                     #  [(4, 0, [record.env.ref('immeuble.res_partner_category').id])]
        #                     #  Key (category_id)=(0) is not present in table "res_partner_category".
        #                       [(0, 8)]
        #                      })  
        for record in self :
            
            # if vals.get('immeuble_ids') :
            if len(record.immeuble_ids) > 0 :
                ###res._add_tag_in_owner()
                # update du dictionnaire
                # Si choix ajout tag category ( celui defini dans le data... xml
                vals.update({'category_id' :
                            #  [(4, 0, [record.env.ref('immeuble.res_partner_category').id])]
                            #  Key (category_id)=(0) is not present in table "res_partner_category".
                              [(4, 8, [record.env.ref('immeuble.res_partner_category').id])]
                             })  
                #               galère de trouver id =8 => "category_id": [    7,    8  ],
                #               tar = 1
                # Si choix remplacement
                # vals.update({
                #     'category_id' :
                #         [(6, 0, [record.env.ref('immeuble.res_partner_category').id])]
                #     })  
                # import pdb; pdb.set_trace()
        return super(ResPartner, self).write(vals)
        
    ## Test fonction nok
    # def _add_tag_in_owner(self):
    #     tag = self.env.ref('res.partner.category')
    #     # ajout du tag voulu
    #     self.id.category_id = [(4, tag.id, 0)]