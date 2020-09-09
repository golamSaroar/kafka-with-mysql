## Kafka Starter with MySQL

The Producer reads json data from an external file and the Consumer inserts the data into a mysql database. 

### Pre-requisites

- Java 8+ (required for Kafka)
- Kafka
- MySQL

But first, rename `config.py.example` to `config.py`. We will use this file in a bit. Also, create a virtual environment and activate it.

### Installing Kafka

Follow this [guideline](https://kafka.apache.org/quickstart) on the official documentation.  
- You should have the Zookeeper service and the Kafka broker service [running](http://kafka.apache.org/documentation/#quickstart_startserver) on your machine.
- Create a topic named `kafka-starter`. (**Note**: This topic name can be anything. If you decide to use some other name, remember to change it accordingly in the `config.py` file)

Also install the kafka-python package: `$ pip install kafka-python`


### Installing MySQL

#### Get the server:  

`$ sudo apt-get update && sudo apt-get install mysql-server`

#### Create user and database:

Replace "username", "password", "newsdb" with the values you've specified in the `config.py` file.  

`$ sudo mysql -u root`

`mysql> USE mysql;`  
`mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';`  
`mysql> GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';`  
`mysql> UPDATE user SET plugin='auth_socket' WHERE User='username';`  
`mysql> FLUSH PRIVILEGES;`  
`mysql> CREATE DATABASE newsdb;`  
`mysql> exit;`  

`$ service mysql restart`  
`$ mysql -u username -p`

#### Get the client:

`$ sudo apt install python3-dev default-libmysqlclient-dev build-essential`  

`$ pip install mysqlclient`

Run `producer.py` from one terminal, and `consumer.py` from another. Check the mysql table to see the values being inserted.