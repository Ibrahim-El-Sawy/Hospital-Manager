# -*- coding: utf-8 -*-

from odoo import models, fields, api ,_


# class Patients(models.Model):
#     _inherit = 'res.partner'
#
#     is_patient = fields.Boolean(string="Is Patient")
#     birthdate = fields.Date(string="Birthdate")
#     age = fields.Integer(string="Age")
#     app_count = fields.Integer(string="Count" , compute='_compute_app_count')
#
#
#     def get_appointments (self):
#         action = {
#             'name' : 'appointments',
#             'res_model' : 'the.appointments',
#             'type': 'ir.actions.act_window',
#             'view_id' : False,
#             'view_mode' : 'tree,form' ,
#         }
#         return action
#
#     def _compute_app_count(self):
#         co = self.env['the.appointments'].search_count([('patient_id' , '=' , self.id)])
#         self.app_count = co


        #   Doctor
# class Doctor(models.Model):
#     _inherit = 'res.users'
#
#     is_doctor = fields.Boolean(string='Is Doctor')
#     is_supervisor = fields.Boolean(string='Is Suprvior')



# class TheAppointments(models.Model):
#     _name = "the.appointments"
#     _description = 'Appointments module'
#     _inherit = ['mail.thread', 'mail.activity.mixin']
#
#     name = fields.Char(string='Appointment Id', required=True, copy=False, readonly=True,
#                        index=True, default=lambda self: _('New'))
#     patient_id = fields.Many2one('hospital.patient', string='Patient', required=True,
#                                  domain="[('is_patient', '=', True)]")
#     patient_age = fields.Integer(string='Age', related='patient_id.age')
#     notes = fields.Text(string='notes')
#     app_date = fields.Datetime(string="Date Time", required=True)
#     state = fields.Selection([
#         ('draft', 'Draft'),
#         ('coniform', 'Coniform'),
#         ('done', 'Done'),
#         ('cancel', 'Cancelled')] , string='Status', default='draft' , readonly=True,)
#     doctor_notes = fields.Text(string="Doctors Notes")
#     prescription_ids = fields.One2many('the.prescription', 'appointment_id')
#     # doctor_id = fields.Many2one('hospital.doctor', string='Doctor', domain="[('is_doctor','=',True)]")
#
#
#     def action_coniform(self):
#         for item in self:
#             item.state = 'coniform'
#     def action_done(self):
#         for item in self:
#             item.state = 'done'
#     def action_cancel(self):
#         for item in self:
#             item.state = 'cancel'
#
#     @api.model
#     def create(self, vals):
#         if vals.get('name', _('New')) == _('New'):
#             vals['name'] = self.env['ir.sequence'].next_by_code('the.appointments.sequence') or _('New')
#         result = super(TheAppointments, self).create(vals)
#         return result


    #    prescription     #
# class Prescription(models.Model):
#     _name = "the.prescription"
#
#     name = fields.Char(string="Medicine Name")
#     notes = fields.Text(string="Notes")
#     appointment_id = fields.Many2one('the.appointments', string="Appointment")
#     medicine_id = fields.Many2one('the.medicine', string="Medicine Name")
#
#
#
#
#  #    medicine
# class Medicine(models.Model):
#     _name = 'the.medicine'
#     _description = 'Medicine module'
#
#     name = fields.Char(string="Medicine_Name")
#     effective_material =  fields.Char(string="Effective Material")
#     is_drug = fields.Boolean("Is Drug")
#     company_name = fields.Char(string="Company Name")
#     unit = fields.Selection([('capsule', 'Capsule'),('table' , 'Table') , ('seachet' , 'Seachet'),('ampule' , 'Ampule') , ('vial','Vial')], default='capsule')
#     presciption_id = fields.One2many('the.prescription', 'medicine_id')




