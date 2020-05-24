from app import db
import datetime


class User(db.Model):
    __tablename__ = 'users'

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
    __tablename__ = 'suppliers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    document = db.Column(db.String(30), nullable=False)
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
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.String(50), nullable=False)
    source = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    document = db.Column(db.String(30), nullable=False)
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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    register_by = db.Column(db.String(100), nullable=False)

    def __init__(self, name, register_by):
        self.name = name
        self.register_by = register_by

    def __repr__(self):
        return "<TerminalType %r>" % self.name

