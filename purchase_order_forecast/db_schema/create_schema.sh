export PATH=/Applications/Postgres.app/Contents/Versions/latest/bin:$PATH
psql -h localhost -U postgres -d Learning -a -f ./schema.sql

