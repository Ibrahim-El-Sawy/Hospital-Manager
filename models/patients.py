from odoo import models, fields, api ,_

from odoo import models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Information"

    # 1. Personal Information

    name = fields.Char(string="Full Name", required=True)
    date_of_birth = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age" , required=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender" , required=True)
    is_patient = fields.Boolean(string="Is Patient", default=True)

    national_id = fields.Char(string="National ID / Passport No." , required=True)
    address = fields.Char(string="Address" , required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    emergency_contact = fields.Char(string="Emergency Contact / Next of Kin")
    marital_status = fields.Selection([
        ('single', 'Single'),
        ('married', 'Married'),
        ('other', 'Other'),
    ], string="Marital Status")
    occupation = fields.Char(string="Occupation")

    # 2. Medical History
    past_illnesses = fields.Text(string="Past Illnesses / Surgeries")
    family_history = fields.Text(string="Family Medical History")
    allergies = fields.Text(string="Allergies")
    immunizations = fields.Text(string="Immunizations / Vaccination Records")
    ongoing_treatments = fields.Text(string="Ongoing Treatments")
    appointment_count = fields.Integer(string=" Appointments", compute="_compute_appointment_count")



    def get_appointments (self):
        action = {
            'name' : 'appointments',
            'res_model' : 'the.appointments',
            'type': 'ir.actions.act_window',
            'view_id' : False,
            'view_mode' : 'tree,form' ,
        }
        return action

    def _compute_appointment_count(self):
        for record in self:
            record.appointment_count = self.env['the.appointments'].search_count([('patient_id', '=', record.id)])

    def action_view_appointments(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'the.appointments',
            'view_mode': 'tree,form',
            'domain': [('patient_id', '=', self.id)],
            'context': {'default_patient_id': self.id}
        }
    # def _compute_app_count(self):
    #     co = self.env['the.appointments'].search_count([('patient_id' , '=' , self.id)])
    #     self.app_count = co
