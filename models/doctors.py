from odoo import models, fields, api

class HospitalDoctor(models.Model):


    _name = "hospital.doctor"
    _description = "Hospital Doctor"


    name = fields.Char(string="Name", required=True)
    specialization = fields.Char(string="Specialization", required=True)
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string="Gender")
    date_of_birth = fields.Date(string="Date of Birth")
    license_number = fields.Char(string="License Number", required=True, copy=False)
    experience_years = fields.Integer(string="Years of Experience", default=0)
    join_date = fields.Date(string="Join Date")
    address = fields.Text(string="Address")
    salary = fields.Float(string="Salary")
    shift = fields.Selection([
        ('morning', 'Morning'),
        ('evening', 'Evening'),
        ('night', 'Night')
    ], string="Shift")
    status = fields.Selection([
        ('active', 'Active'),
        ('leave', 'On Leave'),
        ('retired', 'Retired')
    ], string="Status", default="active")

    is_doctor = fields.Boolean(string='Is Doctor' ,default=True)
    is_supervisor = fields.Boolean(string='Is Suprvior' ,default=True)
    user_id = fields.Many2one('res.users', string="Related User")


    # department_id = fields.Many2one(
    #     'hospital.department',
    #     string="Department"
    # )
