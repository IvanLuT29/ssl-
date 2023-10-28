
Показники моніторингу ЦП і пам'яті:

1. `cpu_usage_percentage`: Вимірює використання ЦП у відсотках, що вказує на завантаження процесора.-
2. `memory_usage_bytes`: відстежує використання пам'яті в байтах, відображаючи використання оперативної пам'яті.
3. `cpu_load_average`: відстежує середнє навантаження ЦП за визначений період часу.
4. `memory_free_bytes`: вказує обсяг вільної пам’яті, доступної.
5. `swap_usage_bytes`: вимірює використання пам’яті підкачки в байтах, надаючи уявлення про використання віртуальної пам’яті.
Всі ці метрики є:  https://www.metricfire.com/blog/tips-for-monitoring-kubernetes-applications/


Метрики моніторингу MySQL:

6. `mysql_up`: вказує, чи працює MySQL Exporter. https://sysdig.com/blog/mysql-monitoring/
7. `mysql_error_count`: відстежує загальну кількість помилок, що виникли в MySQL. https://sysdig.com/blog/mysql-monitoring/
8. `mysql_queries_executed_total`: підраховує загальну кількість запитів, виконаних у MySQL. https://sysdig.com/blog/mysql-monitoring/
9. `mysql_slave_running`: вказує на стан реплікації MySQL   https://bobcares.com/blog/how-to-set-up-database-replication-in-mysql/
10. `mysql_slow_queries_total`: Вимірює загальну кількість виконаних повільних запитів. https://medium.com/@MetricFire/tutorial-monitoring-mysql-server-performance-with-prometheus-and-sql-exporter-714925252632
11. `mysql_connections_active`: відстежує поточну кількість активних підключень MySQL. https://dba.stackexchange.com/questions/270791/getting-current-number-of-connections-in-mysql
12. `mysql_connections_total`: підраховує загальну кількість підключень MySQL. https://dba.stackexchange.com/questions/270791/getting-current-number-of-connections-in-mysql
13. `mysql_innodb_data_reads_total`: вказує загальну кількість читань даних InnoDB. https://dev.mysql.com/doc/mysql-em-plugin/en/myoem-metric-innodb-ioactivity-category.html
14. `mysql_innodb_data_writes_total`: Вимірює загальну кількість записів даних InnoDB. https://dev.mysql.com/doc/mysql-em-plugin/en/myoem-metric-innodb-ioactivity-category.html
15. `mysql_table_locks_immediate`: негайне блокування таблиці, отримане в MySQL. https://dev.mysql.com/doc/refman/8.0/en/lock-tables.html
16. `mysql_table_locks_waited`: кількість запитів на блокування таблиці, які повинні були чекати. https://docs.linuxfabrik.ch/monitoring-plugins/mysql-table-locks.html
17. `mysql_users_connected`: поточна кількість підключених користувачів у MySQL 
18. `mysql_users_queries_total`: сукупна кількість запитів, виконаних кожним користувачем.
19. `mysql_innodb_row_ops_inserts_total`: Загальна кількість операцій вставки рядка InnoDB.
20. `mysql_innodb_row_ops_updates_total`: Загальна кількість операцій оновлення рядка InnoDB.
21. `mysql_query_execution_time_seconds`: відстежує час виконання запитів у секундах.
22. `mysql_table_fragmentation_ratio`: Вимірює коефіцієнт фрагментації таблиць MySQL.
23. `mysql_binlog_events_total`: вказує загальну кількість подій у двійковому журналі. https://dev.mysql.com/doc/refman/8.0/en/show-binlog-events.html
24. `mysql_threads_cached`: відстежує кількість кешованих потоків у MySQL. https://habr.com/ru/articles/159085/
25. `mysql_tmp_disk_tables_created_total`: підраховує загальну кількість створених тимчасових дискових таблиць. https://dba.stackexchange.com/questions/53201/mysql-creates-temporary-tables-on-disk-how-do-i-stop-it