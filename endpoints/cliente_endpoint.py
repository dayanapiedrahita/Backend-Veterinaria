from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.cliente_schema import ClienteCreate, ClienteUpdate, ClienteResponse
from crud.cliente_crud import get_clientes, get_cliente, create_cliente, update_cliente, delete_cliente
from entities.cliente import Cliente

router = APIRouter(prefix="/cliente", tags=["Cliente"])

@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    return get_clientes(db)

@router.get("/{cliente_id}", response_model=ClienteResponse)
def obtener_cliente(cliente_id: int, db: Session = Depends(get_db)):
    cliente = get_cliente(db, cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/", response_model=ClienteResponse)
def crear_cliente(cliente: ClienteCreate, db: Session = Depends(get_db)):
    return create_cliente(db, cliente)

@router.put("/{cliente_id}", response_model=ClienteResponse)
def actualizar_cliente(cliente_id: int, cliente: ClienteUpdate, db: Session = Depends(get_db)):
    updated = update_cliente(db, cliente_id, cliente)
    if not updated:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return updated

@router.delete("/{cliente_id}", response_model=ClienteResponse)
def eliminar_cliente(cliente_id: int, db: Session = Depends(get_db)):
    deleted = delete_cliente(db, cliente_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return deleted