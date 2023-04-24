docker run -it --rm --name rabbitmq -p 15672:15672 --network rabbitmq_network rabbitmq:3.11-management
docker volume create mysql-volume
docker run --name=my-mysql -p3306:3306 --network rabbitmq_network -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=ary123 -d mysql/mysql-server:8.0.20
docker exec -it my-mysql bash
docker run -it --name consumer3 --network rabbitmq_network consumer3


CREATE USER 'root'@'%' IDENTIFIED BY 'PASSWORD';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;

create database Ccproject;
use Ccproject;
create table students(name varchar(40),srn varchar(30),section varchar(10));

