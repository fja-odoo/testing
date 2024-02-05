# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import html
import logging

from odoo import http
from odoo.http import request
from odoo.tools import html2plaintext

_logger = logging.getLogger(__name__)

class ThreeDomTest(http.Controller):

    @http.route(['/testing_og_description'], type='http', auth="public", website=True, sitemap=True)
    def testing(self):
        test_id = request.env['threedom.test'].search([], limit=1)
        unescape_content = html.unescape(html2plaintext(test_id.content))
        values = {
            'content': unescape_content,
        }
        _logger.warning(unescape_content)
        return request.render('threedom_test.testing', values)
