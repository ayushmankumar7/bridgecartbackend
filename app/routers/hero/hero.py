from fastapi import APIRouter,Request,Response,Depends
from db.models.user.user import User
from db.models.hero.hero import Banner,Faq,CTA,Social
from typing import Annotated
from utils.user.auth import IsAuthenticated


router = APIRouter()

# Banner
@router.get("/banner/")
async def get_banner(response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        banners = Banner.get_by_username(username=auth.id)
        return banners
    except Exception as e:
        response.status_code=400 
        return {"error":e}

@router.get("/{username}/banner/")
async def get_username_banner(
                    username: str,
                    response: Response,
                    ):
    try:
        banners = Banner.get_by_username(username=username)
        return banners
    except Exception as e:
        print(e)
        response.status_code=400 
        return {"error":e}

@router.post("/banner/")
async def post_banner(
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        data =await request.json()
        if(type(data)==list):
            for i in data:
                Banner.create(username=auth.id,**i)
        else:
            Banner.create(username=auth.id,**data) 
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}
    
@router.patch("/banner/{id}")
async def update_banner(
                    id: str,
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        data =await request.json()
        Banner.update(username=auth.id,id=id,**data)
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}

@router.delete("/banner/{id}")
async def delete_banner(
                    id: str,
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        Banner.delete(username=auth.id,id=id)
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}


@router.get("/CTA/")
async def get_CTA(response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        CTAData = CTA.get_by_username(username=auth.id)
        return CTAData
    except Exception as e:
        response.status_code=400 
        return {"error":e}

@router.get("/{username}/CTA/")
async def get_username_CTA(
                    username: str,
                    response: Response,
                    ):
    try:
        CTAs = CTA.get_by_username(username=username)
        return CTAs
    except Exception as e:
        print(e)
        response.status_code=400 
        return {"error":e}

@router.post("/CTA/")
async def post_CTA(
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        data =await request.json()
        if(type(data)==list):
            for i in data:
                CTA.create(username=auth.id,**i)
        else:
            CTA.create(username=auth.id,**data) 
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}
    
@router.patch("/CTA/{id}")
async def update_CTA(
                    id: str,
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        data =await request.json()
        CTA.update(username=auth.id,id=id,**data)
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}

@router.delete("/CTA/{id}")
async def delete_CTA(
                    id: str,
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        CTA.delete(username=auth.id,id=id)
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}


@router.get("/Social/")
async def get_Social(response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        Socials = Social.get_by_username(username=auth.id)
        return Socials
    except Exception as e:
        response.status_code=400 
        return {"error":e}

@router.get("/{username}/Social/")
async def get_username_Social(
                    username: str,
                    response: Response,
                    ):
    try:
        Socials = Social.get_by_username(username=username)
        return Socials
    except Exception as e:
        print(e)
        response.status_code=400 
        return {"error":e}

@router.post("/Social/")
async def post_Social(
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        data =await request.json()
        if(type(data)==list):
            for i in data:
                Social.create(username=auth.id,**i)
        else:
            Social.create(username=auth.id,**data) 
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}
    
@router.patch("/Social/{id}")
async def update_Social(
                    id: str,
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        data =await request.json()
        Social.update(username=auth.id,id=id,**data)
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}

@router.delete("/Social/{id}")
async def delete_Social(
                    id: str,
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        Social.delete(username=auth.id,id=id)
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}


@router.get("/Faq/")
async def get_Faq(response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        Faqs = Faq.get_by_username(username=auth.id)
        return Faqs
    except Exception as e:
        response.status_code=400 
        return {"error":e}

@router.get("/{username}/Faq/")
async def get_username_Faq(
                    username: str,
                    response: Response,
                    ):
    try:
        Faqs = Faq.get_by_username(username=username)
        return Faqs
    except Exception as e:
        print(e)
        response.status_code=400 
        return {"error":e}

@router.post("/Faq/")
async def post_Faq(
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        data =await request.json()
        if(type(data)==list):
            for i in data:
                Faq.create(username=auth.id,**i)
        else:
            Faq.create(username=auth.id,**data) 
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}
    
@router.patch("/Faq/{id}")
async def update_Faq(
                    id: str,
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        data =await request.json()
        Faq.update(username=auth.id,id=id,**data)
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}

@router.delete("/Faq/{id}")
async def delete_Faq(
                    id: str,
                    request: Request,
                    response: Response,
                     auth :Annotated[User,"Authentication"] =Depends(IsAuthenticated)
                    ):
    try:
        Faq.delete(username=auth.id,id=id)
        return {"message":"successful"}  
    except Exception as e:
        response.status_code=400 
        return {"error":e}
