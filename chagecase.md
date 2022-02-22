1. In `dbTable.py`, modify line 1 to
   
   `from sqlalchemy import Table, Column, String, create_engine, Integer, Date, MetaData`

2. In `main.py`, add the following line under line 19:

    `metadata = MetaData(engine)`

3. In `main.py`, add the following line under line 22:

    `conn = engine.connect()`

4. In `main.py`, add the following line at the end of the document:

    `conn.close()`