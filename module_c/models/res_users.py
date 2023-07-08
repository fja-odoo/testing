from odoo.addons.module_a.models.res_users import Users as UsersA

def new_foo_a(self):
    print('foo C')

UsersA.foo = new_foo_a
