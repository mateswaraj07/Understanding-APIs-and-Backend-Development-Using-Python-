from fastapi import FastAPI #import FastAPI

app = FastAPI(title="Student API") #creates the application

@app.get("/") #creates a GET endpoint for the root URL
def home():   #defines a function that will be called when the endpoint is accessed
    return {
        "message": "Welcome to Student API"
    }   #sends a JSON response with a welcome message

@app.get("/health") #creates a GET endpoint for the /health URL
def health_check(): #defines a function that will be called when the endpoint is accessed
    return {
        "status": "ok",
        "service": "student-api"
    } #sends a JSON response with the health check information  
# it only tells us that application is responding. It does not prove that the database or every other component is working. It is a simple check to see if the application is running and responding to requests.