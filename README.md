# ees_columns_toggles
Shows column visibility toggles in treeview


USAGE
=====
- 1 Install module
- 2 Restart odoo service - this is necessary to immediately rebuild the assets chache.
- 3 Clear browser cache and goto any odoo page with treeview, that is the table view in odoo wher you would normally have crate / import
- 4 Notice the new button near create or import - use it

This will only allow the fields that are declared in the treeview so you could optionally tweak the tree views you want:
- Open configuration(in debug mode) / technical / user interface / views 
- Filter only tree and search for the model you want to modify the tree.
- If you want the fields to be open by default then add the fields like <field name="email" />
- If you want the fields to be hidden by default, BUT AVAILABLE then add the fields like <field name="email" invisible="1"/>
