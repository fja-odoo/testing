# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Testing',
    'version' : '1.0',
    'summary': 'Testing',
    'sequence': 10,
    'description': """
    Testing
    """,
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'data/threedom_test.xml',
        'views/threedom_test_templates.xml',
    ],
    'license': 'LGPL-3',
}
