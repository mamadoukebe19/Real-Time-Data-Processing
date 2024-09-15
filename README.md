Project Steps 
Step 1: Sign in to AWS Management Console

    Click on the Open Console button, and you will get redirected to AWS Console in a new browser tab.
    On the AWS sign-in page,
        Leave the Account ID as default. Never edit/remove the 12-digit Account ID present in the AWS Console. Otherwise, you cannot proceed with the lab.
        Now copy your Username and Password in the Lab Console to the IAM Username and Password in AWS Console and click on the Sign in button.
    Once Signed in to the AWS Management Console, Make the default AWS Region as US East (N. Virginia) us-east-1.

Step 2: SSH into EC2 Instance

Step 3: Install Docker Compose

1. Download Docker Compose binary:
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

2. Run the below command to make Docker Compose executable:
   sudo chmod +x /usr/local/bin/docker-compose

3. Verify Docker Compose installation:
   docker-compose --version

Step 6: Install PostgreSQL 13 on Amazon Linux 2

1. Update Package Lists:
   sudo yum update -y
2. Add PostgreSQL Repository
   sudo amazon-linux-extras install -y postgresql13
3. Install PostgreSQL:
   sudo yum install -y postgresql13 postgresql13-server
4. Verify PostgreSQL Installation:
   psql --version
5. Add Your User to the Docker Group:
   sudo usermod -aG docker $USER
   
6. Run the below command to apply the changes without logging out:
newgrp docker
7. Run the Application:
   docker-compose up -d

Step 7: Access PostgreSQL Container
1. Run the below command to list all the running containers:
   docker ps
2. Execute the below command to Enter PostgreSQL Container, replace the <container_id> with the container_id of postgresql:
docker exec -it <container_id> /bin/bash
3. Access PostgreSQL CLI:
   psql -U user -d my_database
4. Create a Table inside the Database:
   CREATE TABLE sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ NOT NULL,
    temperature FLOAT,
    humidity FLOAT
);
5. Insert Sample Data to the table:
   INSERT INTO sensor_data (timestamp, temperature, humidity) VALUES
(NOW(), 22.5, 60.0),
(NOW() - INTERVAL '1 hour', 21.0, 65.0);

Step 8: Configure Grafana to connect to this database
1. Navigate to Grafana Dashboard in your browser, replace <EC2_PUBLIC_IP> with Public IPv4 Address:
   http://<EC2_PUBLIC_IP>:3000
4. Go to Connection then select Add new connection:
   ![image](https://github.com/user-attachments/assets/a8787924-de19-4427-bf09-c4b337641d53)
5. Search for postgresql and select postgreSQL:
   ![image](https://github.com/user-attachments/assets/94d91d63-9b11-4784-a2bf-69056553bc03)
6. Click on Add new data source:
   ![image](https://github.com/user-attachments/assets/7ece716c-f993-4857-abf4-01c75222721a)
7. In Connection Enter Host URL as “db:5432” and Database name as “my_database”, in Authentication Enter Username as “user” and Password as “password”, select TLS/SSL Mode as “Disable”, In Additional settings PostgreSQL Options Select Version as “13”. Click on Save & test:
   ![image](https://github.com/user-attachments/assets/8588f99c-9f69-4389-81c9-681c2451d4cd)
Step 9: Create Grafana Dashboards
1. Click on + icon on the top left corner and then select New dashboard
   ![image](https://github.com/user-attachments/assets/e49e25dc-3e9c-4221-9886-0649c1acb752)
2. Click on +Add visualization to create the Dashboard:
   ![image](https://github.com/user-attachments/assets/9824013d-1a72-4279-bb99-36a4027258b1)
3. Select data source as PostgreSQL:
![image](https://github.com/user-attachments/assets/82746bc8-0f93-4dc1-9214-a2d910a039ad)
4. Select code and add the below code and name the Title as Demo_Grafana and Click on Save then add title as Demo and again click on Save:

   SELECT
    timestamp AS "time",
    temperature,
    humidity
FROM
    sensor_data
ORDER BY
    timestamp DESC
LIMIT 10;

![image](https://github.com/user-attachments/assets/d5eb0d98-5b2c-4d47-b536-aa101dab755e)
5. You will see the Dashboard:

![image](https://github.com/user-attachments/assets/508193ee-77bf-49cd-bbda-3d1d96c528c4)
