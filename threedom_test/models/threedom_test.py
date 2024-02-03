from odoo import models, fields


class ThreeDomTest(models.Model):
    _name = 'threedom.test'
    _description = 'ThreeDom Test'

    content = fields.Html('Content', required=True)
