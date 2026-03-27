from fastapi import FastAPI, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistema de Certificación Bancaria")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/certificaciones", response_model=schemas.CertificacionResponse)
def crear_certificacion(
    item: schemas.CertificacionCreate, 
    db: Session = Depends(get_db),
    x_remote_user: Optional[str] = Header(None) 
):
    if not x_remote_user:
        raise HTTPException(status_code=401, detail="Usuario no identificado")

    from datetime import date
    hoy = date.today()
    
    existe = db.query(models.CertificacionProceso).filter(
        models.CertificacionProceso.cod_proceso == item.cod_proceso,
        models.CertificacionProceso.codSucursal == item.codSucursal,
        models.CertificacionProceso.fechaCertificacion == hoy
    ).first()

    if existe:
        raise HTTPException(status_code=400, detail="Este proceso ya fue certificado hoy para esta sucursal")

    nueva_certificacion = models.CertificacionProceso(
        **item.dict(),
        usuario_windows=x_remote_user,
        fechaCertificacion=hoy
    )
    
    db.add(nueva_certificacion)
    db.commit()
    db.refresh(nueva_certificacion)
    return nueva_certificacion