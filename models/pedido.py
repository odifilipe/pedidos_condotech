# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pedido(models.Model):
    _name = 'pedidos.pedido'
    _description = 'Pedido de Cliente'
    _order = 'data_pedido desc'

    name = fields.Char(
        string='Número do Pedido',
        required=True,
        copy=False,
        readonly=True,
        default='Novo'
    )
    
    nome_cliente = fields.Char(
        string='Nome do Cliente',
        required=True,
        help='Nome completo do cliente'
    )
    
    data_pedido = fields.Date(
        string='Data do Pedido',
        required=True,
        default=fields.Date.today,
        help='Data em que o pedido foi criado'
    )
    
    status = fields.Selection([
        ('aberto', 'Aberto'),
        ('processo', 'Em Processo'),
        ('concluido', 'Concluído'),
        ('cancelado', 'Cancelado')
    ], string='Status do Pedido', 
       default='aberto', 
       required=True,
       tracking=True,
       help='Status atual do pedido')
    
    produto_ids = fields.One2many(
        'pedidos.produto',
        'pedido_id',
        string='Produtos',
        help='Lista de produtos incluídos neste pedido'
    )
    
    total_produtos = fields.Integer(
        string='Total de Produtos',
        compute='_compute_total_produtos',
        store=True
    )
    
    valor_total = fields.Float(
        string='Valor Total',
        compute='_compute_valor_total',
        store=True,
        digits=(12, 2)
    )

    @api.depends('produto_ids')
    def _compute_total_produtos(self):
        """Calcula o total de produtos no pedido"""
        for pedido in self:
            pedido.total_produtos = len(pedido.produto_ids)

    @api.depends('produto_ids.preco_unitario')
    def _compute_valor_total(self):
        """Calcula o valor total do pedido"""
        for pedido in self:
            pedido.valor_total = sum(pedido.produto_ids.mapped('preco_unitario'))

    @api.model_create_multi
    def create(self, vals_list):
        """Gera numeração sequencial para o pedido"""
        for vals in vals_list:
            if vals.get('name', 'Novo') == 'Novo':
                vals['name'] = self.env['ir.sequence'].next_by_code('pedidos.pedido') or 'Novo'
        return super().create(vals_list)

    def action_iniciar_processo(self):
        """Muda o status do pedido para 'Em Processo'"""
        self.ensure_one()
        self.status = 'processo'

    def action_concluir(self):
        """Muda o status do pedido para 'Concluído'"""
        self.ensure_one()
        self.status = 'concluido'

    def action_cancelar(self):
        """Muda o status do pedido para 'Cancelado'"""
        self.ensure_one()
        self.status = 'cancelado'

    def action_reabrir(self):
        """Reabre um pedido cancelado"""
        self.ensure_one()
        self.status = 'aberto'