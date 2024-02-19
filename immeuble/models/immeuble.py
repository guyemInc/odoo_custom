from odoo import models, fields, api

class Immeuble(models.Model):
    _name = 'immeuble'
    _description = 'immeuble'
    _order = 'id desc'

    name = fields.Char(
        string='Nom de l\'immeuble',
        required=True
    )
    building_value = fields.Float(
        string='Prix estimé',
        default=0.0,
        required=False
    )
    floor_count = fields.Integer(
        string='Nb d\'étages',
        default=1,
        required=True
    )
    adress_street = fields.Char(
        string='Rue',
        required=True
    )
    # adress_test = fields.Char(
    #     string='Rue',
    #     required=True,
    #     oldname='adress_street'
    # )
    adress_town = fields.Char(
        string='Ville',
        required=True
    )
    country_id = fields.Many2one(
        'res.country',
        # compute='_compute_account_root'
        string='Pays',
        required=False
    )
    owner_id = fields.Many2one(
        'res.partner',
        string='Proprietaire',
        required=False
    )
    state_id = fields.Many2one(
        'immeuble.state',
        string='Statut',
        required=False
    )

    immeuble_tag_ids = fields.Many2many(
        'immeuble.tag', 
        string='Tags', 
        help="Optional tags to your Immeuble", 
        ondelete='restrict')
    
    #immeuble_ids = fields.One2many('immeuble', 'owner_id',  string='Proprietaire')
    immeuble_offer_ids = fields.One2many('immeuble.offre', 
        'immeuble_id', 
        string='Offres')
    # category_ids = fields.Many2many(
    #     'hr.employee.category', 'employee_category_rel',
    #     'emp_id', 'category_id', groups="hr.group_hr_user",
    #     string='Tags')

    offre_count = fields.Integer(
        string='Nb offres',        
        compute = '_compute_offre_count'
    )

    # Demonstration d'une recherche groupée dans le dataset
    # Avec également le debugger console : pdb
    # def _compute_offre_count(self):
    #     data = self.env['immeuble.offre'].read_group(
    #         [('immeuble_id', '=',self.ids)],
    #         ['immeuble_id'],
    #         ['immeuble_id']
    #     )
    #     mapped_data = {m['immeuble_id'][0] : m['immeuble_id_count'] for m in data}
    #     import pdb; pdb.set_trace()

    def _compute_offre_count(self):
        for record in self :
            # offres = len(self.env['immeuble.offre'].search([
            #     ('immeuble_id', '=',record.id)
            # ]))            
            record.offre_count = len(
                self.env['immeuble.offre'].search([
                    ('immeuble_id', '=', record.id)
                ])
            )
    @api.model
    def create(self,vals):
        res = super(Immeuble, self).create(vals)
        if res.owner_id :
            #res._add_tag_in_owner()
            # Ici maj de la valeur
            # res.owner_id.write({
            #     'name' : 'toto',
            #     'phone' : '1234567890',
            #     email' : 'test'
            # })
            # Ici maj attribut custom
            if res.owner_id.description_test != 'NoText' :
                res.owner_id.write({
                    # 'name' : 'toto',
                    # 'phone' : '1234567890',
                     'description_test' : res.owner_id.name + ' Add text from Immeuble function create if owner_id'
                    # 'description_test' : ' Blabla from Immeuble function create if owner_id'
                })
            else   :
                res.owner_id.write({
                    # 'name' : 'toto',
                    # 'phone' : '1234567890',
                    'description_test' : 'NoText'
                    #'email' : 'test'
                }) 
        return res