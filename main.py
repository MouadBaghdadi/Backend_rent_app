from fastapi import FastAPI, Request
from .models import models
from . import schemas
from .database import engine
from .routers import annonce, googleauth, user, favannonce, authentification, scrap
from fastapi_jwt_auth.exceptions import AuthJWTException
from .settings import Settings
from fastapi.responses import JSONResponse
from fastapi_jwt_auth import AuthJWT
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # React application's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

app.include_router(annonce.router)
# app.include_router(user.router)
# app.include_router(favannonce.router)
app.include_router(authentification.router)
app.include_router(googleauth.router)
app.include_router(scrap.router)

@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={'detail': exc.message}
    )




if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

    
