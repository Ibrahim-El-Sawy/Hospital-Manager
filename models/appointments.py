from odoo import models, fields, api ,_
class TheAppointments(models.Model):
    _name = "the.appointments"
    _description = 'Appointments module'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Appointment Id', required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True,
                                 domain="[('is_patient', '=', True)]")
    patient_age = fields.Integer(string='Age', related='patient_id.age')

    notes = fields.Text(string='notes')
    app_date = fields.Datetime(string="Date Time", required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('coniform', 'Coniform'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')] , string='Status', default='draft' , readonly=True,)
    doctor_notes = fields.Text(string="Doctors Notes")
    prescription_ids = fields.One2many('the.prescription', 'appointment_id')
    doctor_id = fields.Many2one('hospital.doctor', string='Doctor', domain="[('is_doctor','=',True)]")
    val1 = fields.Integer('val1')
    val2 = fields.Integer('Val2')
    val3 = fields.Integer(compute='_compute_val3')

    def action_coniform(self):
        for item in self:
            item.state = 'coniform'
    def action_done(self):
        for item in self:
            item.state = 'done'
    def action_cancel(self):
        for item in self:
            item.state = 'cancel'

    @api.depends('val1', 'val2' , 'prescription_ids.medicine_id.name')
    def _compute_val3(self):
        for doc in self:
         doc.val3 = doc.val1 + doc.val2

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('the.appointments.sequence') or _('New')
        result = super(TheAppointments, self).create(vals)
        return result
