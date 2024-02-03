# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import html

from odoo import http
from odoo.http import request
from odoo.tools import html2plaintext


class ThreeDomTest(http.Controller):

    @http.route(['/testing_og_description'], type='http', auth="public", website=True, sitemap=True)
    def testing(self):
        test_id = request.env['threedom.test'].search([], limit=1)
        values = {
            'content': html.unescape(html2plaintext(test_id.content)),
        }
        return request.render('threedom_test.testing', values)
