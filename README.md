# 📦 Módulo Pedidos - CondoTech

Sistema de gestão de pedidos de clientes desenvolvido para Odoo 18.0.

![Odoo](https://img.shields.io/badge/Odoo-18.0-714B67?style=flat-square&logo=odoo)

## 📋 Descrição

O módulo **Pedidos** foi desenvolvido como desafio técnico para a Porter. Ele permite acompanhar o processo de venda, desde a criação do pedido até a entrega final, com controle de status e gestão de produtos.

## ✨ Funcionalidades

### Gestão de Pedidos
- ✅ Numeração automática e sequencial de pedidos (PED00001, PED00002, etc.)
- ✅ Cadastro de pedidos com informações do cliente (Básico)
- ✅ Controle de workflow com 4 status: Aberto, Em Processo, Concluído e Cancelado
- ✅ Botões de ação contextuais para mudança de status
- ✅ Visualização do status em barra de progresso (statusbar)
- ✅ Cálculo automático do total de produtos e valor total do pedido
- ✅ Possibilidade de reabrir pedidos cancelados

### Gestão de Produtos
- ✅ Cadastro de produtos vinculados a pedidos (Básico)
- ✅ Campos: Nome, Descrição e Preço Unitário
- ✅ Relacionamento Many2one com pedidos
- ✅ Visualização inline dos produtos dentro do pedido
- ✅ Edição rápida na lista de produtos (editable="bottom")

### Segurança
- 🔒 Controles de acesso configurados
- 🗑️ Exclusão em cascata de produtos ao deletar pedido

## 🛠️ Requisitos

- **Odoo**: 18.0
- **Dependências Odoo**: `base`

## 📦 Instalação

### 1. Clone ou copie o módulo

```bash
cd /caminho/para/odoo/addons
git clone [https://github.com/odifilipe/pedidos_condotech.git](https://github.com/odifilipe/pedidos_condotech.git)

### 2. Atualize a lista de aplicativos (talvez seja necessário reiniciar o Odoo)

No Odoo, acesse: 
    Aplicativos → Atualizar lista de aplicativos (executar no modo de debug)

### 3. Instale o módulo

Busque por "Pedidos" e clique em "Ativar"

### 4. Uso

#### Criando um Pedido
1. Acesse Pedidos → Pedidos → Novo
2. Preencha o nome do cliente
3. A data será preenchida automaticamente (editável)
4. Adicione produtos na aba Produtos
5. Salve o pedido (numeração automática será gerada)

#### Botões disponíveis:

- Iniciar Processo: Muda status de "Aberto" para "Em Processo"
- Concluir Pedido: Muda status de "Em Processo" para "Concluído"
- Cancelar: Cancela o pedido (disponível em Aberto e Em Processo)
- Reabrir: Reabre um pedido cancelado

#### Filtrando Pedidos
Use os filtros pré-configurados:

- Por Status: Abertos, Em Processo, Concluídos, Cancelados
- Por Data: Pedidos de Hoje
- Agrupamentos: Status, Cliente, Data do Pedido