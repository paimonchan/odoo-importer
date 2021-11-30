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
        
        for row in rows:
            row[0]  # for each iterate will print `name`, `product 01`, `product 02`
            row[1]  # for each iterate will print `description`, `product 01 desc`, `product 02 desc`
            row[2]  # for each iterate will print `date`, datetime(2021-11-31), datetime(2021-11-15)