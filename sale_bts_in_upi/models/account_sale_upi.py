# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import base64

from odoo import models
from odoo.tools.image import image_data_uri


class SalesOrderUpi(models.Model):
    _inherit = "sale.order"

    def _salegenerate_qr_code(self, silent_errors=False):
        self.ensure_one()
        if self.company_id.country_code == 'IN':
            qr_code_url = 'upi://pay?pa=%s&pn=%s&am=%s&tr=%s&tn=%s' % (
                self.company_id.l10n_in_upi_id,
                self.company_id.name,)
            barcode = self.env['ir.actions.report'].barcode(barcode_type="QR", value=qr_code_url, width=120, height=120)
            return image_data_uri(base64.b64encode(barcode))
        return super()._salegenerate_qr_code(silent_errors)

