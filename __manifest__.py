{
    'name': 'Product Stock',
    'sequence': 1,
    'version': '16.0.1.0.0',
    'depends': ['base', 'website_sale'],

    'data': [
        'views/stock_availability.xml',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,

}
