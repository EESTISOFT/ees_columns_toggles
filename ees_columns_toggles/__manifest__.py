{
    'name': 'Columns visibility toggles for treeview',
    'version': '11.0.4.8',
    'author': 'Hideki Yamamoto',
    'category': 'Productivity',
    'website': 'https://www.eestisoft.com',
    'sequence': 2,
    'summary': 'Allows to toggle visibility of columns for every treeview in odoo',
    'description': """

Columns toggles for treeview

 Substantial rework of sunpop.cn 'app_dynamic_list' module to achieve compatibility with odoo 11 and 12

============
Allows to switch visibility of individual columns in odoo.

Steps:
1-Install module
2-Restart odoo service - this is important for somewhat reason.
3-Clear browser cache and goto any odoo page with treeview, that is the table view in odoo wher you would normally have crate / import
4-Notice the new button near create or import - use it

This will only allow the fields that are declared in the treeview so you could optionally tweak the tree views you want:
-Open configuration(in debug mode) / technical / user interface / views 
-Filter only tree and search for the model you want to modify the tree.
-If you want the fields to be open by default then add the fields like <field name="email" />
-If you want the fields to be hidden by default, BUT AVAILABLE then add the fields like <field name="email" invisible="1"/>

Made with love.

    """,
    'images': [],
    'depends': ['web'],
    'data': [
		'views/ees_columns_toggles.xml',
    ],	
    'qweb': ['static/src/xml/ees_columns_toggles_button.xml'],
    'installable': True,
    'application': True,
    'auto_install': False
}