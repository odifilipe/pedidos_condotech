{
    'name': 'Pedidos',
    'version': '0.1',    
    'category': 'Sales',
    'summary': 'Sistema de gestão de pedidos de clientes',
    'description':  """
        Módulo de gestão de pedidos para a CondoTech
        =============================================
        
        Funcionalidades:
        * Gerenciamento de pedidos de clientes
        * Controle de produtos por pedido
        * Workflow com status personalizados
        * Relacionamento One2many entre Pedidos e Produtos
    """,
    'author': 'Odi Filipe',
    'website': 'https://github.com/odifilipe/pedidos_condotech',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/pedido_views.xml',
        'views/produto_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}