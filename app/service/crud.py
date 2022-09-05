from fastapi.encoders import jsonable_encoder
from sqlalchemy.future import select
from db.db import async_session


async def create(Model, data):
    data.id = None
    async with async_session() as session:
        data_dict = jsonable_encoder(data)
        db_row = Model(**data_dict)
        session.add(db_row)
        await session.commit()
        await session.refresh(db_row)
    return db_row


async def journal_create(JournalBase, JournalExtend, JournalMerge, data):
    data.id = None
    async with async_session() as session:
        data_dict = jsonable_encoder(data)

        db_row1 = JournalBase(**data_dict)

        session.add(db_row1)
        await session.commit()
        await session.refresh(db_row1)

        data_dict['id'] = db_row1.id
        db_row2 = JournalExtend(**data_dict)

        session.add(db_row2)
        await session.commit()
        await session.refresh(db_row2)

        data_dict = jsonable_encoder(db_row1) | jsonable_encoder(db_row2)

    return JournalMerge(**data_dict)


async def update(Model, data):
    async with async_session() as session:
        data_dict = jsonable_encoder(data)
        db_row = await session.get(Model, data.id)
        for var, value in data_dict.items():
            setattr(db_row, var, value)
        session.add(db_row)
        await session.commit()
        await session.refresh(db_row)
    return db_row


async def journal_update(JournalBase, JournalExtend, JournalMerge, data):
    db_row1 = update(JournalBase, data)
    db_row2 = update(JournalExtend, data)
    data_dict = jsonable_encoder(db_row1) | jsonable_encoder(db_row2)
    return JournalMerge(**data_dict)


async def read(Model, id):
    async with async_session() as session:
        return await session.get(Model, id)


async def read_all(Model):
    async with async_session() as session:
        query = select(Model)
        results = await session.execute(query)
    return results.scalars()


async def delete(Model, id):
    async with async_session() as session:
        db_row = await session.get(Model, id)
        session.delete(db_row)
        await session.commit()
        await session.refresh(db_row)
    return True
