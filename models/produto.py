# -*- coding: utf-8 -*-

from odoo import models, fields


class Produto(models.Model):
    _name = 'pedidos.produto'
    _description = 'Produto do Pedido'

    nome_produto = fields.Char(
        string='Nome do Produto',
        required=True,
        help='Nome ou descrição curta do produto'
    )
    
    descricao = fields.Text(
        string='Descrição',
        help='Descrição detalhada do produto'
    )
    
    preco_unitario = fields.Float(
        string='Preço Unitário',
        required=True,
        digits=(12, 2),
        help='Preço unitário do produto'
    )
    
    pedido_id = fields.Many2one(
        'pedidos.pedido',
        string='Pedido',
        required=True,
        ondelete='cascade',
        help='Pedido ao qual este produto pertence'
    )
    
    cliente = fields.Char(
        related='pedido_id.nome_cliente',
        string='Cliente',
        store=True,
        readonly=True
    )