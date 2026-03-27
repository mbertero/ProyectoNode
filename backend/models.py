from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date, Time, Text
from .database import Base
import datetime

class Proceso(Base):
    __tablename__ = "procesos"
    
    cod_proceso = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombreProceso = Column(String(255), nullable=False)
    estadoProceso = Column(Integer, default=1) 
    periodicidadProceso = Column(String(50)) 
    hora_limite_atencion = Column(Time, nullable=True)
    observacion = Column(Text, nullable=True)

class CertificacionProceso(Base):
    __tablename__ = "certificacionProcesos"
    
    codCertificacion = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cod_proceso = Column(Integer, ForeignKey("procesos.cod_proceso"))
    codSucursal = Column(String(50), nullable=False)
    usuario_windows = Column(String(100), nullable=False)
    fechaCertificacion = Column(Date, nullable=False)
    estado_certificacion = Column(String(20)) 
    observacion = Column(Text, nullable=True)
    timestampregistro = Column(DateTime, default=datetime.datetime.utcnow)