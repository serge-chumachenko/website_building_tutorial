# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Teachers(models.Model):
    _name = 'website_building_tutorial.teachers'

    name = fields.Char("Teacher's Name")
    biography = fields.Html("Teacher's biography")
    course_ids = fields.One2many('website_building_tutorial.courses', 'teacher_id', "Course")

class Courses(models.Model):
    _name = 'website_building_tutorial.courses'
    _inherit = 'mail.thread'

    name = fields.Char("Course's Name")
    teacher_id = fields.Many2one('website_building_tutorial.teachers', "Teacher")
