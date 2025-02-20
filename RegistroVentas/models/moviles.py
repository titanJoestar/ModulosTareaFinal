from odoo import models, fields, api

class Moviles(models.Model):
    _name = 'moviles'
    _description = 'Registro de ventas de móviles'

    telefono = fields.Many2one(
        'movil',
        string="Modelo de móvil",
        required=True
    )
    precioventa = fields.Float(
        string="Precio de Venta",
        compute='_compute_precioventa',
        store=True
    )
    cantidad = fields.Integer(
        string="Cantidad",
        required=True,
        default=1
    )
    preciototal = fields.Float(
        string="Total",
        compute='_compute_preciototal',
        store=True
    )

    # Cálculo del precio con margen del 20%
    @api.depends('telefono')
    def _compute_precioventa(self):
        for record in self:
            record.precioventa = record.telefono.precio * 1.20 if record.telefono else 0.0

    # Cálculo del total
    @api.depends('precioventa', 'cantidad')
    def _compute_preciototal(self):
        for record in self:
            record.preciototal = record.precioventa * record.cantidad

    # Validación de tipo para IDs
    @api.model
    def create(self, vals):
        if 'telefono' in vals:
            vals['telefono'] = int(vals['telefono'])  # Forzar conversión a entero
        return super().create(vals)

    def write(self, vals):
        if 'telefono' in vals:
            vals['telefono'] = int(vals['telefono'])  # Forzar conversión a entero
        return super().write(vals)

    # Método para mostrar "Venta nºX" en lugar de "Moviles,X"
    def name_get(self):
        result = []
        for record in self:
            name = f"Venta nº{record.id}"  # Formato personalizado
            result.append((record.id, name))
        return result
