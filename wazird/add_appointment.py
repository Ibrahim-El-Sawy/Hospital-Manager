from odoo import models, fields


class AddAppointmentWizard(models.TransientModel):
    _name = 'add.appointment'

    notes = fields.Text(string='notes')
    app_date = fields.Datetime(string="Date Time", required=True)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True ,
                                 domain=[('is_patient', '=', 'True')],ondelete="cascade")
    doctor_id = fields.Many2one('hospital.doctor', required=True, string='Doctor',
                                domain="[('is_doctor','=',True)]")

    def confirm_appointment(self):

            vals = {
                'patient_id': self.patient_id.id,
                'notes': self.notes,
                'app_date': self.app_date,
                'doctor_id': self.doctor_id.id
            }
            self.env['the.appointments'].create(vals)