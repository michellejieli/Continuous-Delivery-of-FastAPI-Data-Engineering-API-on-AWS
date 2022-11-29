# Project 4 -  Continuous Delivery of FastAPI Data Engineering API on AWS

## Key Objectives

I built a microservice that suggests a recipe idea when you query a food or ingredient. The data comes from [Yummly API](https://rapidapi.com/apidojo/api/yummly2). The JSON payload will result in a dictionary containing 2 keys - ingredients and searhes. The value for for ingredients is a list of food items containing the queried ingredient and the value for the searches is a list of recipes containing the queried ingredient. 

## Workflow Diagram
![ML_proj_4 (1)](https://user-images.githubusercontent.com/70456530/204614296-dd8fb125-8a05-40f2-8f89-e15c864ce0e5.png)

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

## Example 
### Input: 
/recipe/avocado

### Output: 
`{'ingredients': ['avocado', 'avocados', 'avocado oil', 'hass avocados', 'hass avocado', 'ripe avocados', 'large avocados', 'medium avocado', 'haas avocados', 'california avocado', 'california avocados', 'small avocados', 'small avocado', 'fresh avocado', 'avocado leaves', 'florida avocado', 'fresh california avocado, ripe', 'fresh california avocados, ripe', 'fresh california avocados', 'large california avocados', 'large california avocado', 'olivado avocado oil', 'fresh california avocado', 'baby avocados', 'wholly avocado', 'la tourangelle avocado oil', 'mission avocados', 'california haas avocados', 'fuerte avocado', 'jumbo avocado', 'farm rich avocado slices', 'hidden valley® original ranch® avocado dressing', 'spectrum avocado oil'], 'searches': ['avocado', 'avocado salad', 'chicken avocado', 'avocado sauce', 'avocado tomato', 'avocado sandwich', 'avocado low carb', 'avocado onion tomato dip', 'cold avocado soup', 'avocado artichoke']}'`
