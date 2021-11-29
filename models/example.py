from odoo import models

class Example(models.TransientModel):
    _name = 'paimon.example'
    _inherit = 'paimon.importer'