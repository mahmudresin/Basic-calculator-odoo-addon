from odoo import http
from odoo.http import request
import json

class CalculatorController(http.Controller): 
    @http.route('/calculator/calculate', type = 'json', auth = 'user')
    def calculate(self, expression): 
        try: 
            #security - only allow certain character and functions
            allowed_chars = set('0123456789+=*/().%')
            if not all(c in allowed_chars for c in expression):
                return {'error': 'Invalid characters in expression'}
            
            # Evaluate the expression safety
            result = eval(expression,{"__builtins__":{}})
            
            # Save to history
            history = request.env['calculator.history'].create_history(expression, result)
            
            return{
                'result' : result, 
                'history_id' : history.id
            }
        except Exception as e:
            return {'error': str(e)}
         
    
    @http.route('/calculator/history', type = 'json', auth = 'user')
    def get_history(self, limit = 10): 
        histories = request.env['calculator.history'].search(
            [('user_id','=',request.env.user.id)],
            limit = limit, order = 'create_date desc'
        )   
        
        return [{
            'id' : h.id, 
            'expression': h.expression, 
            'result' : h.result, 
            'date' : h.create_date
        } for h in histories ] 
            