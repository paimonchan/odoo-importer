from odoo import models

class Example(models.TransientModel):
    _name = 'paimon.example'
    _inherit = 'paimon.importer'

    def output_xls(self, rows):
        """
        # @INPUT EXCEL
        =============================================================
        | name              | description           | date          |
        -------------------------------------------------------------
        | product 01        | product 01 desc       | 2021-11-31    |
        -------------------------------------------------------------
        | product 02        | product 02 desc       | 2021-11-15    |
        ------------------------------------------------------------
        """
        pass