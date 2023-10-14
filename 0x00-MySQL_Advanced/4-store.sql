--Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.c
DELIMITER //
CREATE TRIGGER DecreaseQuantityAfterOrder
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Decrease the quantity of the item in the 'items' table
    UPDATE items
    SET quantity = quantity - NEW.quantity
    WHERE item_id = NEW.item_id;
END;
//
DELIMITER ;
