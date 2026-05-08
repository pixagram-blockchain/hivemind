DROP FUNCTION IF EXISTS hivemind_postgrest_utilities.check_community;
CREATE OR REPLACE FUNCTION hivemind_postgrest_utilities.check_community(_name TEXT)
  RETURNS BOOLEAN
  LANGUAGE plpgsql
  IMMUTABLE
AS
$BODY$
BEGIN
  IF _name IS NOT NULL AND
    LENGTH(_name) > 7 AND
    SUBSTRING(_name FROM 1 FOR 7) = 'portal-' AND
    SUBSTRING(_name FROM 8 FOR 1) IN ('1', '2', '3') AND
    _name ~ '^portal-[123]\d{4,6}$' THEN

    RETURN TRUE;
  ELSE

    RETURN FALSE;
  END IF;
END;
$BODY$
;