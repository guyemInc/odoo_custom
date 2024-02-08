{
    'name': 'Immeuble',
    'version': '1.0',
    'description': 'Description toute simple',
    'summary': 'Sommaire tout simple',
    'author': 'un autheur',
    'website': 'un site web',
    'license': 'LGPL-3',
    'category': 'custom',
    'depends': [
        'base',
        'contacts'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/immeubles_views.xml',
        'views/immeubles_tag_views.xml',
        'views/immeubles_state_views.xml',
        'views/infrastructures_views.xml',
        'views/immeubles_offres_views.xml',
        'views/owner_views.xml',
        'data/immeuble_tag_data.xml'
    ],
    # 'demo': [
    #     ''
    # ],
    # 'auto_install': False,
    # 'application': False,
    # 'assets': {
        
    # }
}