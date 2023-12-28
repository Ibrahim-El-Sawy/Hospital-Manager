# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Patients(models.Model):
    _inherit = 'res.partner'

    is_patient = fields.Boolean(string="Is Patient")


class ResUsers(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean(string='Is Doctor')

