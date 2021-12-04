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

        :param rows:                list values rows in excel 

        :Example:
        rows = [
            ('name', 'description', 'date),
            ('product 01', 'product 01 desc', datetime(2021-11-31)),
            ('product 02', 'product 02 desc', datetime(2021-11-15))
        ]
        """
        
        for row in rows:
            row[0]  # for each iterate will print `name`, `product 01`, `product 02`
            row[1]  # for each iterate will print `description`, `product 01 desc`, `product 02 desc`
            row[2]  # for each iterate will print `date`, datetime(2021-11-31), datetime(2021-11-15)

        # breakdown
        # row 1
        rows[0][0]  # print `name`
        rows[0][1]  # print `description`
        rows[0][2]  # print `date`
        # row 2
        rows[1][0]  # print `product 01`
        rows[1][1]  # pring `product 01 desc`
        rows[1][2]  # print `datetime(2021-11-31)`
        # row 3
        rows[1][0]  # print `product 02`
        rows[1][1]  # pring `product 02 desc`
        rows[1][2]  # print `datetime(2021-11-15)`