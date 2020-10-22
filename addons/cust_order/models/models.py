#-*- coding: utf-8 -*-

from odoo import models, fields, api


class cust_order(models.Model):
	_name = 'cust_order.cust_order'
	_description = 'cust_order.cust_order'
	
	order_number=fields.Char()
	order_revision=fields.Char()
	order_date=fields.Date()
	order_revision_date=fields.Date()
	order_file_name=fields.Char()
	order_created_by=fields.Char()
	order_revision_date=fields.Date()
	order_current_buyer=fields.Char()
	order_payment_terms=fields.Char()
	order_due_date=fields.Date()
	
class cust_order_line(models.Model):
	_name = 'cust_order.cust_order.cust_order_line'
	_description = 'cust_order.cust_order.cust_order_line'
	order_number=fields.Char()
	order_line_no=fields.Integer()
	part_number=fields.Char()
	part_qty=fields.Integer()
	part_uom=fields.Char()
	part_unit_price=fields.Float()		
	part_description=fields.Char()
	order_line_amount=fields.Float()
	order_line_dummy=fields.Char()
