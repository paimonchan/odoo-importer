import base64
from odoo import models, fields

class Importer(models.TransientModel):
    _name = 'paimon.importer'

    file = fields.Binary(required=True)

    def _create_import_entry(self):
        import_model = self.env['base_import.import']
        import_entry = import_model.create(dict(file=base64.b64decode(self.file)))
        return import_entry
    
    def _validate_columns_type(self, rows):
        types = self.column_types()
        if not types:
            return
        for columns, type in types.items():
            # TODO: add checking type data here
            pass

    def import_xls(self):
        import_entry = self._create_import_entry()
        rows = import_entry._read_xls()
        self._validate_columns_type(rows)
        self.output_xls(rows)

    def import_csv(self):
        import_entry = self._create_import_entry()
        options = dict(quoting='|', separator=',')  
        rows = import_entry._read_csv(options)
        self._validate_columns_type(rows)
        self.output_csv(rows)

    def output_xls(self, rows):
        # override function
        pass

    def output_csv(self, rows):
        # override function
        pass

    def output_ods(self):
        # override function
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