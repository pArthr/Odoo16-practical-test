# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Odoo Practical Test (Split Delivery Order Based on Planned Date)',
    'version': '16.0.1.0.0',
    'category': 'Sales,Warehouse',
    'description' : '''
       This module helps to split Do based on sale order lines planned date.
    ''',
    'summary': 'This module helps to split Do based on sale order lines planned date.'
    'author': 'Parth Trivedi',
    'depends': ['sale','sale_stock'],
    'data': [
        'views/sale.xml',
    ],
    'demo': [],
    'test': [],
    'license': 'AGPL-3',
    'installable' : True,
    'auto_install' : False,
    'application' : True,
    'pre_init_hook': 'pre_init_check',
	
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
