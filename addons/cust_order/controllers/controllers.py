# -*- coding: utf-8 -*-
# from odoo import http


# class CustOrder(http.Controller):
#     @http.route('/cust_order/cust_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cust_order/cust_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('cust_order.listing', {
#             'root': '/cust_order/cust_order',
#             'objects': http.request.env['cust_order.cust_order'].search([]),
#         })

#     @http.route('/cust_order/cust_order/objects/<model("cust_order.cust_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cust_order.object', {
#             'object': obj
#         })
