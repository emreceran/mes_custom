# -*- coding: utf-8 -*-
##############################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
##############################################################################
from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    section_ids = fields.One2many(
        'section.line', 'purchase_order_id', "Sections")

    @api.model
    def create(self, vals):
        res = super(PurchaseOrder, self).create(vals)
        section_dict = {}
        line_total = []
        for line in res.order_line:
            if not line.display_type:
                line_total.append(line.price_subtotal)
            elif line.display_type == 'line_section':
                section_dict[line.name] = line_total
                line_total = []
            if line.display_type == 'line_section':
                section_dict[line.name] = line_total
        for sections in section_dict:
            section_vals = {
                'section_name': sections,
                'total': sum(section_dict[sections]),
                'purchase_order_id': res.id,
                'currency_id': res.currency_id and res.currency_id.id or False
            }
            res.write({
                'section_ids': [(0, 0, section_vals)]
            })
        for l in res.order_line:
            if l.display_type == 'line_section':
                if l.name in section_dict:
                    l.section_total = \
                        str(l.currency_id.symbol) + ' ' + \
                        "{:0.2f}".format(sum(section_dict[l.name]))
        return res

    def write(self, vals):
        res = super(PurchaseOrder, self).write(vals)
        if vals.get('order_line'):
            section_dict = {}
            line_total = []
            self.section_ids.unlink()
            for line in self.order_line:
                if not line.display_type:
                    line_total.append(line.price_subtotal)
                elif line.display_type == 'line_section':
                    section_dict[line.name] = line_total
                    line_total = []

                if line.display_type == 'line_section':
                    section_dict[line.name] = line_total
            for sections in section_dict:
                section_vals = {
                    'section_name': sections,
                    'total': sum(section_dict[sections]),
                    'purchase_order_id': self.id,
                    'currency_id': self.currency_id and self.currency_id.id
                                   or False,
                }
                self.write({
                    'section_ids': [(0, 0, section_vals)]
                })
            for l in self.order_line:
                if l.display_type == 'line_section':
                    if l.name in section_dict:
                        l.section_total =\
                            str(l.currency_id.symbol) + ' ' + \
                            "{:0.2f}".format(sum(section_dict[l.name]))
        return res


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    section_total = fields.Char('Section total', default='0.00')

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4
