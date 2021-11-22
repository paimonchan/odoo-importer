from odoo import models, fields

class Importer(models.TransientModel):
    _name = 'paimon.importer'

    def output_xls():
    file = fields.Binary(required=True)

    def _create_import_entry(self):
        pass

        pass

    def output_csv():
        pass

    def output_ods():
        pass

    def columns_type():
        # TODO: create inheritable function to store typedata per columns
        return False