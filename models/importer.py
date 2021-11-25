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

    def import_csv(self):
        import_entry = self._create_import_entry()
        options = {}
        rows = import_entry._read_csv(options)
        self.output_csv(rows)

    def output_xls(self, rows):
        pass

    def output_csv(self):
        pass

    def output_ods(self):
        pass

    def column_types(self):
        """
        example: {
            0 : {
                type    : Integer | String | Date,
                require : True | False
            },
            1 : {
                type    : Integer | String | Date,
                require : True | False
            }
        }
        NOTE: 0 and 1 is column number start from left to right.
        """
        return False