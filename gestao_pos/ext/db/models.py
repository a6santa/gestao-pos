# -*- encoding: utf-8 -*-
from datetime import datetime
from werkzeug.security import check_password_hash
from gestao_pos.ext.db import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    permission = db.Column(db.Enum('admin', 'operator'), name='permission')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

    def __init__(self, username, password, name, email, permission='operator', status=True):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.permission = permission
        self.status = status

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return "<User %r>" % self.username


class Supplier(db.Model):
    __tablename__ = 'supplier'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    document = db.Column(db.String(30), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(14), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                           onupdate=datetime.datetime.utcnow, nullable=False)
    status = db.Column(db.Boolean, default=True)
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, name, document, address, email, number,
                 city, state, zip_code, register_by, status=True):
        self.name = name
        self.document = document
        self.address = address
        self.email = email
        self.number = number
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.register_by = register_by
        self.status = status

    def __repr__(self):
        return "<Suplier %r>" % self.name


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    document = db.Column(db.String(30), nullable=False, unique=True)
    address = db.Column(db.String(200), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(255), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zip_code = db.Column(db.String(14), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                           onupdate=datetime.datetime.utcnow, nullable=False)
    status = db.Column(db.Boolean, default=True)
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, source_id, source, name, document, address, email, number,
                 city, state, zip_code, register_by, status=True):
        self.source_id = source_id
        self.source = source
        self.name = name
        self.document = document
        self.address = address
        self.email = email
        self.number = number
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.register_by = register_by
        self.status = status

    def __repr__(self):
        return "<Customer %r>" % self.name


class TerminalState(db.Model):
    __tablename__ = 'terminal_state'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, name, register_by):
        self.name = name
        self.register_by = register_by

    def __repr__(self):
        return "<TerminalState %r>" % self.name


class TerminalType(db.Model):
    __tablename__ = 'terminal_type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, name, register_by):
        self.name = name
        self.register_by = register_by

    def __repr__(self):
        return "<TerminalType %r>" % self.name


class Terminal(db.Model):
    __tablename__ = 'terminal'

    id = db.Column(db.Integer, primary_key=True)
    nota_fiscal = db.Column(db.String(50), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    model = db.Column(db.String(255), nullable=False)
    terminal_type_id = db.Column(db.Integer, db.ForeignKey('terminal_type.id'), nullable=False)
    terminal_type = db.relationship("TerminalType", backref=db.backref("terminal", lazy=True))
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    supplier = db.relationship("Supplier", backref=db.backref("terminal", lazy=True))
    serial_number = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    terminal_state_id = db.Column(db.Integer, db.ForeignKey('terminal_state.id'), nullable=False)
    terminal_state = db.relationship("TerminalState", backref=db.backref("terminal", lazy=True))
    purchase_price = db.Column(db.DECIMAL(14, 4), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                           onupdate=datetime.datetime.utcnow, nullable=False)
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, brand, model, terminal_type_id, supplier_id, serial_number,
                 terminal_state_id, purchase_price, register_by, status=True):
        self.brand = brand
        self.model = model
        self.terminal_type_id = terminal_type_id
        self.supplier_id = supplier_id
        self.serial_number = serial_number
        self.terminal_state_id = terminal_state_id
        self.purchase_price = purchase_price
        self.status = status
        self.register_by = register_by

    def __repr__(self):
        return "<Terminal %r>" % self.serial_number


class TerminalMovement(db.Model):
    __tablename__ = 'terminal_movement'

    id = db.Column(db.Integer, primary_key=True)
    terminal_id = db.Column(db.Integer, db.ForeignKey('terminal.id'), nullable=False)
    terminal = db.relationship("Terminal", backref=db.backref("terminal_movement", lazy=True))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship("Customer", backref=db.backref("terminal_movement", lazy=True))
    price = db.Column(db.DECIMAL(14, 4), nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    movement_type = db.Column(db.Enum('venda', 'aluguel', 'manutenção'), name='movement_type')
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, terminal_id, customer_id, price, start_date, end_date, movement_type, register_by):
        self.terminal_id = terminal_id
        self.customer_id = customer_id
        self.price = price
        self.start_date = start_date
        self.end_date = end_date
        self.movement_type = movement_type
        self.register_by = register_by

    def __repr__(self):
        return "<TerminalMovement %r>" % self.id


class Supply(db.Model):
    __tablename__ = 'supply'

    id = db.Column(db.Integer, primary_key=True)
    nota_fiscal = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'), nullable=False)
    supplier = db.relationship("Supplier", backref=db.backref("supply", lazy=True))
    purchase_price = db.Column(db.DECIMAL(14, 4), nullable=False)
    qtd = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow,
                           onupdate=datetime.datetime.utcnow, nullable=False)
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, nota_fiscal, name, brand, supplier_id, purchase_price, qtd, register_by):
        self.nota_fiscal = nota_fiscal
        self.name = name
        self.brand = brand
        self.supplier_id = supplier_id
        self.purchase_price = purchase_price
        self.qtd = qtd
        self.register_by = register_by

    def __repr__(self):
        return "<Supply %r>" % self.name


class SupplyMovement(db.Model):
    __tablename__ = 'supply_movement'

    id = db.Column(db.Integer, primary_key=True)
    supply_id = db.Column(db.Integer, db.ForeignKey('supply.id'), nullable=False)
    supply = db.relationship("Supply", backref=db.backref("supply_movement", lazy=True))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship("Customer", backref=db.backref("supply_movement", lazy=True))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    qtd = db.Column(db.Integer, nullable=False)
    price = db.Column(db.DECIMAL(14, 4), nullable=False)
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, supply_id, customer_id, created_at, qtd, price, register_by):
        self.supply_id = supply_id
        self.customer_id = customer_id
        self.created_at = created_at
        self.price = price
        self.qtd = qtd
        self.register_by = register_by

    def __repr__(self):
        return "<SupplyMovement %r>" % self.id
