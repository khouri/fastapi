from fastapi import APIRouter, HTTPException, status, Body, Depends, Request
from models.events import Event, EventUpdate
from typing import List
from database.connection import get_session

event_router = APIRouter(
    tags = ["Events"]
)

events_lst = []

@event_router.get("/", response_model=List[Event])
async def retrieve_all_Events(session = Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return(events)


@event_router.get("/{id}", response_model=Event)
async def retrieve_single_event(id:int, session = Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return(event)

    raise HTTPException(
                        status_code = status.HTTP_404_NOT_FOUND,
                        detail = "Event with supplied ID does not exist"
                       )

@event_router.post("/new")
async def create_event(new_event:Event,
                       session = Depends(get_session)) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return(
            {"message":"Event created sucessfully"}
          )


@event_router.delete("/{id}")
async def delete_event(id:int) -> dict:
    for event in events_lst:
        if event.id == id:
            events_lst.remove(event)
            return({"message":"Event deleted successfully"})
        raise HTTPException(
                            status_code = status.HTTP_404_NOT_FOUND,
                            detail = "Event with supplied ID does not exist"
                           )


@event_router.delete("/")
async def delete_all_evenst() -> dict:
    events_lst.clear()
    return({"message":"Events deleted successfully"})


@event_router.put("/edit/{id}", response_model=Event)
async def update_event(id:int,
                       newdata:EventUpdate,
                       session = Depends(get_session)) -> Event:

    event = session.get(Event, id)
    if event:
        event_data = newdata.dict(exclude_unset = True)
        for key, value in event_data.items():
            setattr(event, key, value)

        session.add(event_data)
        session.commit()
        session.refresh(event_data)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
