# # # -*- coding: utf-8 -*-
#
# from odoo import models, fields, api
#
#
# class sozen_reports(models.Model):
#     _inherit='project.project'
#
#     def get_panel_data(self):
#         self.ensure_one()
#         if not self.user_has_groups('base.group_system'):
#         # if not self.user_has_groups('project.group_project_user'):
#             return {}
#         panel_data = {
#             'user': self._get_user_values(),
#             'buttons': sorted(self._get_stat_buttons(), key=lambda k: k['sequence']),
#             'currency_id': self.currency_id.id,
#         }
#         if self.allow_milestones:
#             panel_data['milestones'] = self._get_milestones()
#         if self._show_profitability():
#             profitability_items = self._get_profitability_items()
#             if self._get_profitability_sequence_per_invoice_type() and profitability_items and 'revenues' in profitability_items and 'costs' in profitability_items:  # sort the data values
#                 profitability_items['revenues']['data'] = sorted(profitability_items['revenues']['data'], key=lambda k: k['sequence'])
#                 profitability_items['costs']['data'] = sorted(profitability_items['costs']['data'], key=lambda k: k['sequence'])
#             panel_data['profitability_items'] = profitability_items
#             panel_data['profitability_labels'] = self._get_profitability_labels()
#         return panel_data
#
# #
# # #     _name = 'sozen_reports.sozen_reports'
# # #     _description = 'sozen_reports.sozen_reports'
# #
# # #     name = fields.Char()
# # #     value = fields.Integer()
# # #     value2 = fields.Float(compute="_value_pc", store=True)
# # #     description = fields.Text()
# # #
# # #     @api.depends('value')
# # #     def _value_pc(self):
# # #         for record in self:
# # #             record.value2 = float(record.value) / 100
