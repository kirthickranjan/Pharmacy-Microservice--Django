**Required Softwares:**
1. Python
2. pip
3. MySQL
4. Node Js
5. virtualenv


**DataBases and Tables:**
1. user_mgmt
   - Table : user
2. prescription_db
   - Table : prescriptions
3. stock_db
   - Table : orders,products

**
Setup the Service for each Services:**

1. Auth Service (Port 8076)
   
       cd auth-service
       python -m virtualenv venv
       venv\Scripts\activate
       pip install -r requirements.txt
       python django startproject auth_service .
       python manage.py startapp users
       python manage.py makemigrations
       python manage.py migrate
   
2. Prescription Service (Port 8081)

       cd prescription-service
       python -m virtualenv venv
       venv\Scripts\activate
       pip install -r requirements.txt
       python django startproject priscription_service .
       python manage.py startapp prescriptions
       python manage.py makemigrations
       python manage.py migrate

3. Stock Service (Port 8082)
   
       cd stock-service
       python -m virtualenv venv
       venv\Scripts\activate
       pip install -r requirements.txt
       python django startproject stck_service .
       python manage.py startapp stocks
       python manage.py makemigrations
       python manage.py migrate

4.API Gateway (Port 8080)

      cd api-gateway
      python -m virtualenv venv
      venv\Scripts\activate
      pip install -r requirements.txt
      python django startproject api-gateway .
      python manage.py startapp gateway
      python manage.py makemigrations
      python manage.py migrate

5. React Frontend (Port 3000)
   
       cd pharmacy-frontend
       npm install

**
Running the Application:
Start Services in Order**

Terminal 1: Auth Service

       cd auth-service
       python manage.py runserver 8076
       
Terminal 2: Prescription Service

     cd prescription-service
     python manage.py runserver 8081
     
Terminal 3: Stock Service

     cd stock-service
     python manage.py runserver 8082
     
Terminal 4: API Gateway

     cd api-gateway
     python manage.py runserver 8080
     
Terminal 5: React Frontend

     cd pharmacy-frontend
     npm start

**
The Following API's used in the application are:**
1. http://localhost:8076/health → Auth Service
2. http://localhost:8081/api/v1/prescription/health → Prescription Service
3. http://localhost:8082/api/v1/products/health → Stock Service
4. http://localhost:8080/health → API Gateway
5. http://localhost:3000 → Frontend

