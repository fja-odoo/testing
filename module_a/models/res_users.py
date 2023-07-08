from odoo import models


class Users(models.Model):
    _inherit = 'res.users'

    def foo(self):
        print('foo A')
