from odoo import models, fields

class WaterRegion(models.Model):
    _name = "water.region"
    _description = "Region codes from water source Spain"
    
    code = fields.Char(string="Region Code", required=True)
    name = fields.Char(string="Region Name", required=True)
    
    _sql_constraints = [
        ('code_unique', 'unique(code)', 'Each region must have a unique code.')
    ]