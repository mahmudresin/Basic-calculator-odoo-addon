# calculator_app/models/calculator_history.py
from odoo import api, fields, models, _

class CalculatorHistory(models.Model):
    _name = 'calculator.history'
    _description = 'Calculator History'
    _order = 'create_date desc'

    name = fields.Char(string='Operation', required=True)
    expression = fields.Char(string='Expression', required=True)
    result = fields.Float(string='Result', required=True)
    user_id = fields.Many2one('res.users', string='User', default=lambda self: self.env.user)
    create_date = fields.Datetime('Creation Date', readonly=True)

    @api.model
    def create_history(self, expression, result):
        return self.create({
            'name': expression + ' = ' + str(result),
            'expression': expression,
            'result': result
        })