# Michelle_Li_Project_4 -  Continuous Delivery of Flask/FastAPI Data Engineering API on AWS

## Key Objectives

I built a microservice that suggests a recipe idea when you query a food or ingredient. The data comes from [Yummly API](https://rapidapi.com/apidojo/api/yummly2). The JSON payload will result in a dictionary containing 2 keys - ingredients and searhes. The value for for ingredients is a list of food items containing the queried ingredient and the value for the searches is a list of recipes containing the queried ingredient. 

## Workflow Diagram
![ML_proj_4](https://user-images.githubusercontent.com/70456530/204611087-ef46d376-031d-4be2-a6fd-0c1c734f3935.png)

## Workflow Steps 

### 1. Create Python script leveraging [Yummly API](https://rapidapi.com/apidojo/api/yummly2) and FastAPI.
* Store data as a JSON object.
* Display web API using FastAPI. 

### 2. Containerize FastAPI and push to AWS ECR 
* Copy Github repo in AWS Cloud9 environment.
* Create image in ECR.
* In Cloud9 terminal, use commands from 'View push commands' in ECR to push FastAPI to ECR. 

### 3. Deploy containerized API using AWS App Runner.
* Create service and choose image for source.

### 4. Perform continuous delivery using AWS CodeBuild.
* Create build project and choose Github project for source. 
