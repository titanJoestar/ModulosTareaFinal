from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Movil(models.Model):
    _name = 'movil'
    _description = 'Dispositivos móviles disponibles'

    sistemaoperativo = fields.Selection(
        [('android', 'Android'), ('ios', 'iOS')],
        string="Sistema Operativo",
        required=True
    )
    marca = fields.Char(string="Marca", required=True, size=113)  # Longitud máxima controlada
    gigas = fields.Integer(string="Almacenamiento (GB)", required=True)
    color = fields.Char(string="Color", required=True)
    precio = fields.Float(string="Precio Base", required=True)

    @api.constrains('marca')
    def _check_marca_length(self):
        for record in self:
            if len(record.marca) < 1 or len(record.marca) > 113:
                raise ValidationError("La marca debe tener entre 1 y 113 caracteres")

    def name_get(self):
        return [(rec.id, rec.marca) for rec in self]
