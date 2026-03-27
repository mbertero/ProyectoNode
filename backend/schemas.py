from pydantic import BaseModel
from datetime import date, datetime, time
from typing import Optional

class ProcesoBase(BaseModel):
    cod_proceso: int
    nombreProceso: str
    periodicidadProceso: str
    hora_limite_atencion: Optional[time] = None
    observacion: Optional[str] = None

    class Config:
        from_attributes = True

class CertificacionCreate(BaseModel):
    cod_proceso: int
    codSucursal: str
    estado_certificacion: str 
    observacion: Optional[str] = None

class CertificacionResponse(CertificacionCreate):
    codCertificacion: int
    usuario_windows: str
    fechaCertificacion: date
    timestampregistro: datetime

    class Config:
        from_attributes = True