import base64
from odoo import models, fields

class Importer(models.TransientModel):
    _name = 'paimon.importer'

    file = fields.Binary(required=True)

    def _create_import_entry(self):
        import_model = self.env['base_import.import']
        import_entry = import_model.create(dict(file=base64.b64decode(self.file)))
        return import_entry
    
    def _validate_columns_type(self, row):
        types = self.column_types()
        if not types:
            return
        for columns, type in types.items():
            # TODO: add checking type data here
            pass

    def import_xls(self):
        import_entry = self._create_import_entry()
        rows = import_entry._read_xls()
        self.output_xls(rows)

    def output_xls(self, rows):
        pass

    def output_csv(self):
        pass

    def output_ods(self):
        pass

    def column_types(self):
        # TODO: create inheritable function to store typedata per columns
        return False