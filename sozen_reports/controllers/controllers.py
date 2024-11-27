 # -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request

class WebsiteForm(http.Controller):
   @http.route(['/Harcamalar'], type='http', auth="public", website=True)
   def appointment(self):
       projects = request.env['project.project'].sudo().search([])

       values = {}
       values.update({
           'projects': projects
       })
       print(values)
       return request.render("sozen_reports.harcama_page", values)
       # return "Hello world"



# from odoo import http
# from odoo.http import request
#
# class WebsiteForm(http.Controller):
#    @http.route(['/Harcamalar'], type='http', auth="user", website=True)
#    def appointment(self):
#        partners = request.env['project.task'].sudo().search([])
#        values = {}
#        values.update({
#            'partners': partners
#        })
#        return request.render("sozen_reports.form_harcama", values)

# class SozenReports(http.Controller):
#     @http.route('/sozen_reports/sozen_reports', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sozen_reports/sozen_reports/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sozen_reports.listing', {
#             'root': '/sozen_reports/sozen_reports',
#             'objects': http.request.env['sozen_reports.sozen_reports'].search([]),
#         })

#     @http.route('/sozen_reports/sozen_reports/objects/<model("sozen_reports.sozen_reports"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sozen_reports.object', {
#             'object': obj
#         })
