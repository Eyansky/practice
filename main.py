from fastapi import FastAPI

app = FastAPI()

app.get("/")
def home():
    """ welcome message """
    return {"greetings" :"welcome"}

if __name__ == "__main__":
    uvicorn.run(app,port=8000)