# Rebuild SQL Database
1. Open MySQL Workbench, create a new schema called `bt2102_as_1`
2. "Server"-"Data Import"
3. Under "Import Options", select "Import from Dump Project Folder", and choose the folder of this repository.
4. "Start Import"
5. Double click the schema `bt2102_as_1` to set it to the default working schema.
6. Run the mySQL instructions in the file `set_nullable_return_date.sql`.
7. Run the mySQL instructions in the file `Add current book borrowed.sql`.
8. Done!