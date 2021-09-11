from flask_sqlalchemy import SQLAlchemy, model
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from datetime import datetime

db = SQLAlchemy()


class CuentaPagos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_registro = db.Column(db.DateTime, default=datetime.now)
    nombre_paciente = db.Column(db.String(128))
    fecha_pago =  db.Column(db.DateTime,nullable=True)
    valor_pago = db.Column(db.Integer)    
    confirmacion_pago = db.Column(db.Boolean, default=False, nullable=False)

class CuentaPagosSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CuentaPagos
        load_instance = True


def __repr__(self):
    return "{}-{}-{}-{}-{}".format(self.fecha_registro,self.nombre_paciente,self.fecha_pago,self.valor_pago,self.confirmacion_pago)