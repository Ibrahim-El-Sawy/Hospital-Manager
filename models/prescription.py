from odoo import models, fields, api ,_


class Prescription(models.Model):
    _name = "the.prescription"

    name = fields.Char(string="Medicine Name")
    notes = fields.Text(string="Notes")
    appointment_id = fields.Many2one('the.appointments', string="Appointment")
    medicine_id = fields.Many2one('the.medicine', string="Medicine Name")




 #    medicine
class Medicine(models.Model):
    _name = 'the.medicine'
    _description = 'Medicine module'

    name = fields.Char(string="Medicine_Name")
    effective_material =  fields.Char(string="Effective Material")
    is_drug = fields.Boolean("Is Drug")
    company_name = fields.Char(string="Company Name")
    unit = fields.Selection([('capsule', 'Capsule'),('table' , 'Table') , ('seachet' , 'Seachet'),('ampule' , 'Ampule') , ('vial','Vial')], default='capsule')
    presciption_id = fields.One2many('the.prescription', 'medicine_id')
