# -*- coding: utf-8 -*-
{
    'name': "Hospital Manager",
    'summary': "Product for hospitals and patients",
    'description': """
          using this module for complete manage your hospital and get good reports 
    """,
    'author': "alMohamady",
    'website': "https://www.alMohamady.com",
    'category': 'Uncategorized',
    'version': '0.1.1',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wazird/add_appointment_view.xml',
        'views/templates.xml',
        'data/data.xml',
        'views/views.xml',
        'views/doctors.xml',
        'views/appointments.xml',
        'views/medicine.xml',
        'views/menus.xml',
    ],
}

