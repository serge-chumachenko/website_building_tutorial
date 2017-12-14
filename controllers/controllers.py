# -*- coding: utf-8 -*-
from odoo import http


class Academy(http.Controller):
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['website_building_tutorial.teachers']
        return http.request.render('website_building_tutorial.index', {
            'teachers': Teachers.search([]),
        })

    @http.route('/academy/<model("website_building_tutorial.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('website_building_tutorial.biography', {
            'person': teacher
        })
    # @http.route('/academy/<int:id>/', auth='public', website=True)
    # def teacher(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    # @http.route('/academy/<name>/', auth='public', website=True)
    # def teacher(self, name):
    #     return '<h1>{}</h1>'.format(name)

# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kwargs):
#         return "Hello, World!"

# class Academy(http.Controller):
#     @http.route('/academy/academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/academy/academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('academy.listing', {
#             'root': '/academy/academy',
#             'objects': http.request.env['academy.academy'].search([]),
#         })

#     @http.route('/academy/academy/objects/<model("academy.academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('academy.object', {
#             'object': obj
#         })