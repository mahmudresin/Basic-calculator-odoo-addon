# calculator_app/__manifest__.py
{
    'name': 'Calculator',
    'version': '1.0',
    'summary': 'Basic Calculator for Odoo',
    'description': '''
        This module adds a calculator functionality to Odoo.
        Features:
        - Basic arithmetic operations
        - Memory functions
        - Calculation history
    ''',
    'author': 'Yeamin Mahmud Resin',
    'website': 'yeaminmahmudres.vercel.app',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/calculator_security.xml',
        'security/ir.model.access.csv',
        'views/calculator_views.xml',
        'views/calculator_templates.xml',
        'views/calculator_menu.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'calculator_app/static/src/js/calculator.js',
            'calculator_app/static/src/css/calculator.css',
            'calculator_app/static/src/xml/templates.xml',
        ],
    },
    'license': 'LGPL-3',
    'application': True,
    'installable': True,
    'auto_install': False,
}