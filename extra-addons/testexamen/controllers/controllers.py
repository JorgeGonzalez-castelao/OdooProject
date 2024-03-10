# -*- coding: utf-8 -*-
# from odoo import http


# class Testexamen(http.Controller):
#     @http.route('/testexamen/testexamen', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testexamen/testexamen/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('testexamen.listing', {
#             'root': '/testexamen/testexamen',
#             'objects': http.request.env['testexamen.testexamen'].search([]),
#         })

#     @http.route('/testexamen/testexamen/objects/<model("testexamen.testexamen"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testexamen.object', {
#             'object': obj
#         })
