kubectl run mysql --image=mysql --restart=Never --env="MYSQL_ROOT_PASSWORD=123abc" --port=3306
kubectl expose pod mysql --type=NodePort --port=3306
192.168.123.130:31427

CREATE DATABASE `cge3` DEFAULT CHARACTER SET utf8;
INSERT INTO cge.metadata (country) VALUES ("Poland");
INSERT INTO cge.metadata (country, latitude, longitude) VALUES ("Poland", 55.123456, 80.123456);
SELECT * FROM cge.metadata;

$ kubectl exec -it mysql -- bash
$ mysql --user=root --password

> show databases;
> create database <db_name>;
> use <db_name>;
> show tables;
> select * from <table_name>;

mysqldump --password --all-databases > all_databases.sql
mysql --password < all_databases.sql



kubectl exec -n global-sewage sewage-db-6cdb5d49b8-fn5xw -- sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /nfs/data/global-sewage/production/storage/sewage-db/backup/alldbs.sql

kubectl exec -n global-sewage $(kubectl get pod -n global-sewage | grep sewage-db | cut -f1 -d" ") -- sh -c 'exec mysqldump --all-databases -uroot -p"$MYSQL_ROOT_PASSWORD"' > /nfs/data/global-sewage/production/storage/sewage-db/backup/$(date +%s)alldbs.sql
