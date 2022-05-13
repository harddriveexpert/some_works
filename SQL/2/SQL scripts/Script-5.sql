create extension if not exists pgcrypto;
CREATE FUNCTION encrypt_value_supplier() RETURNS TRIGGER AS $$
    BEGIN
        NEW.sex = PGP_SYM_ENCRYPT(NEW.sex ,'AES_KEY');
        RETURN NEW;
    END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER encrypt_row_supplier
    BEFORE INSERT on person
    FOR EACH ROW
    EXECUTE PROCEDURE encrypt_value_supplier();