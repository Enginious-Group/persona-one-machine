import io
import os
import pathlib
import shutil
import subprocess
from zipfile import ZipFile


from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI, File, UploadFile
from starlette.responses import RedirectResponse, FileResponse, HTMLResponse
from PIL import Image

from api import *
from my_image_processing import MyModel  # TODO edit change to your model


class Message(BaseModel):
    message: str


def read_imagefile(file) -> Image.Image:
    image = Image.open(io.BytesIO(file))
    return image

state = {}

app_desc = """<h2> Persona ML API </h2>
use `/process/my_method` endpoint to process image
<br>by Appsilon"""

app = FastAPI(title='Persona API', description=app_desc, debug=True)


@app.on_event("startup")
async def load_model():
    state['model'] = MyModel()  # TODO choose your model


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


@app.post(
    "/process/my_method",  # TODO edit endpoint name

    responses={
        200: {
            "content": {"zip": {}},
            "description": "Returns processed image",
        },
        422: {"model": Message},
        500: {"model": Message},
    }
)
async def process_api(file: UploadFile = File(...)):


    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return HTMLResponse({"message": "Image must be jpg or png format!"}, status_code=422)

    image = read_imagefile(await file.read())

    try:
        res = state['model'].process_image(image) 
        res.save("result.png")
        topologypath = 'D:\\Persona\\Maya\\input\\baked_new_topology.obj'
        olddiffusepath = 'D:\\Persona\\FBX\\baked_diffuse.png'
        oldFbxpath = 'D:\\Persona\\FBX\\wrappedHead_v001.fbx'
        if os.path.exists(topologypath):
            os.remove(topologypath)
        if os.path.exists(olddiffusepath):
            os.remove(olddiffusepath)
        if os.path.exists(oldFbxpath):
            os.remove(oldFbxpath)

        
        goodname= "ML_Head.png"
        pathout = pathlib.Path('D:/Persona/Maya/Input')
        path = pathlib.Path('result.png')
        dirname = os.path.dirname(path)
        newname = os.path.join(pathout, goodname)
        shutil.copyfile(path, newname)
        newname = pathlib.Path(newname)
        process_file(newname, pathout)
        # 
        subprocess.call([r'D:\Persona\Maya\HBaker_v003.bat'])

        with ZipFile('response.zip', 'w') as response_zip:
            response_zip.write(r"D:\\Persona\\FBX\\baked_diffuse.png", "baked_diffuse.png")
            response_zip.write(r"D:\\Persona\\FBX\\wrappedHead_v001.fbx", "wrappedHead_v001.fbx")
        
        return FileResponse("response.zip", media_type="zip")
        # return FileResponse("result.png", media_type="image/png")
    except Exception as e:
        # TODO edit possibly adjust error message
        message = "Something went wrong during image processing"
        if app.debug:
            message += f"\n{e}"
        return HTMLResponse(message, status_code=500)

if __name__ == "__main__":
    # TODO edit turn off debug, change port if using python api.py to run
    uvicorn.run(app, debug=True, port=9092, host="0.0.0.0")
