ALTER TABLE `bt2102_as_1`.`LibMember` 
ADD COLUMN `current_books_borrowed` INT NOT NULL AFTER `outstanding_fee`;

ALTER TABLE `bt2102_as_1`.`LibMember` 
ADD COLUMN `current_books_reserved` INT NOT NULL AFTER `current_books_borrowed`;