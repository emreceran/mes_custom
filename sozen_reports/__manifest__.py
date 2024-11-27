# -*- coding: utf-8 -*-
{
    'name': "sozen_reports",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My ",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'project', ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',

#        'views/form_harcama.xml',
 #       'views/templates.xml',
        # 'views/app.xml',
        # 'views/project.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    "assets": {
        "web.assets_qweb": [
            # "account_financial_report/static/src/js/report_action.esm.js",
  #          "sozen_reports/static/src/xml/**/*",
        ],

    },
}
