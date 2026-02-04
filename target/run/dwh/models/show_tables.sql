
    create view `claude_db`.`show_tables__dbt_tmp` as
        SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'claude_db'
ORDER BY table_name