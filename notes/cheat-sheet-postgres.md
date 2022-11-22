# Cheat Sheet Postgres

### Show active queries that's been running for x period of time

```sql
SELECT pid, now() - pg_stat_activity.query_start AS duration, query, state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '1 minutes'
AND state = 'active';
```

### Kill running query

```sql
SELECT pg_cancel_backend(pid);
```

### Table and index size

```sql
SELECT
   relname table_name,
   pg_size_pretty(pg_total_relation_size(relid)) "Total Size",
   pg_size_pretty(pg_indexes_size(relid)) "Index Size",
   pg_size_pretty(pg_relation_size(relid)) "Table Size"
FROM pg_statio_user_tables
ORDER BY pg_total_relation_size(relid) DESC;
```

### Show total number of dead tuples

Dead tuples - deleted rows

Returns the total number of dead tuples to be vacuumed

```sql
SELECT relname, n_dead_tup FROM pg_stat_user_tables;
```

### Last vacuum and analyze time

```sql
SELECT relname,last_vacuum, last_autovacuum, last_analyze, last_autoanalyze
FROM pg_stat_user_tables;
```
