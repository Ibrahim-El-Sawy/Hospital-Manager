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
        'reports/report_appointment.xml',
        'wazird/add_appointment_view.xml',
        'views/templates.xml',
        'data/data.xml',
        'views/views.xml',
        'views/prescription.xml',
        'views/patients.xml',
        'views/doctors.xml',
        'views/appointments.xml',
        'views/search_appointment.xml',
        'views/medicine.xml',
        'views/menus.xml',
    ],
    'assets':{
        'web.assets_backend' :['my_hospital/static/src/css/appointment.css']
    }
}

