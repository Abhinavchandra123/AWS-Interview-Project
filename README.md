# AWS Interview Project – Full Implementation

This repository contains the complete AWS cloud infrastructure and backend API setup built according to the interview assignment requirements.

---

## 🌐 Static Website (Task 1)
A public S3 static website was created and configured.

🔗 **S3 Static Website URL:**  
http://abhinav-static-website-s3-bucket.s3-website.ap-south-1.amazonaws.com/

---

## 🏗 Architecture Overview
- Custom VPC (public + private subnets)
- NAT Gateway + Internet Gateway
- EC2 instance in private subnet running a Flask API
- Application Load Balancer in public subnets
- DynamoDB database for storing items
- CloudWatch logs + alarms
- IAM roles for secure access management

---

## 🖥 Backend API – Load Balancer DNS
All API calls go through the public ALB endpoint.

🔗 **ALB DNS:**  
http://interview-alb-996235617.ap-south-1.elb.amazonaws.com/

---

## 🔧 Flask API (`app.py`)
The API supports the following endpoints:

### ✔ Home
```
GET /
```

### ✔ Create Item  
```
POST /item
Content-Type: application/json
{"id": "1", "value": "hello"}
```

### ✔ Get Item  
```
GET /item/1
```

---

## 🧪 Testing the API

```
curl http://interview-alb-996235617.ap-south-1.elb.amazonaws.com/

curl -X POST http://interview-alb-996235617.ap-south-1.elb.amazonaws.com/item      -H "Content-Type: application/json"      -d '{"id":"1","value":"hello"}'

curl http://interview-alb-996235617.ap-south-1.elb.amazonaws.com/item/1
```

---

## 🗄 DynamoDB Table
- Table Name: **InterviewTable**
- Partition Key: **id**

Used to store and retrieve API records.

---

## 📜 CloudWatch Logs
CloudWatch Agent collects:

- `/var/log/messages`
- `/home/ec2-user/app.log`

ALB access logs stored in S3.

---

## 🔔 CloudWatch Alarm
Alarm created for:

- **CPU Utilization > 70%**
- Sends notification via **SNS email**

---

## 🔐 IAM Roles
EC2 Instance Role includes:

- DynamoDB read/write permissions  
- CloudWatch Logs write permissions  
- SSM for console access  
- S3 PutObject (for ALB access logs)

---

## 📁 Folder Structure
```
├── app.py
├── README.md
└── screenshots/
```

---

## ✅ Summary
This project demonstrates AWS networking, compute, storage, security, monitoring, and backend API development—fully aligned with real-world cloud architecture patterns.

