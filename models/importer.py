import base64
from odoo import models, fields

class Importer(models.TransientModel):
    _name = 'paimon.importer'

    file = fields.Binary(required=True)

    def _create_import_entry(self):
        import_model = self.env['base_import.import']
        import_entry = import_model.create(dict(file=base64.b64decode(self.file)))

    def output_xls(self):
        pass

    def output_csv(self):
        pass

    def output_ods(self):
        pass

    def columns_type(self):
        # TODO: create inheritable function to store typedata per columns
        return False