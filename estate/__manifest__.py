# -*- coding: utf-8 -*-
{
    'name': "Real Estate",
    'summary': """
        Starting module for "Real Estate"
    """,

    'description': """
        Starting module for "Real Estate"
    """,

    'version': '0.1',
    'application': True,
    'category': 'Tutorials/Estate',
    'installable': True,
    'depends': ['base', 'web'],
    'data': [
        "security/ir.model.access.csv",
        "views/estate_menus.xml",
        "views/estate_property_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_type_views.xml",
        "views/res_users_views.xml",
    ],
    'assets': {
        'web.assets_backend': [

        ],
    },
    'license': 'AGPL-3'
}
