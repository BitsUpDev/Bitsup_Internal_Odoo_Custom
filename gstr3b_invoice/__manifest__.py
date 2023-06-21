# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Odoo GSTR3B - Returns And Invoices",
  "summary"              :  """Odoo GSTR3B - Returns And Invoices allows you to get the Simplified GSTR Summary in JSON format which can be directly uploaded to file GSTR3B.""",
  "category"             :  "Accounting",
  "version"              :  "1.0.1",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo-GSTR3B-Returns-And-Invoices.html",
  "description"          :  """Odoo GSTR3B - Return And Invoices
GSTR3B
Odoo GSTR3b
GST
GST Module
GSTR3B returns
File GSTR3b via Odoo
Tax filing
Odoo Tax GSTR3B
GSTR3B Tax
GSTR 3B Filing
GSTR-3B - Return Filing
GST returns
GSTR3B - Return And Invoices via Odoo""",
  "live_test_url"        :  "https://odoodemo.webkul.com/demo_feedback?module=gstr3b_invoice",
  "depends"              :  ['gst_invoice'],
  "data"                 :  [
                             'views/gstr3_view.xml',
                             'views/product_view.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  49,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
}
