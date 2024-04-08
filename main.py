import os
import sys
os.system('pip install websockets --upgrade')
os.system('pip install sanic --upgrade')

import sanic
import aiohttp
import uvloop
import json
import asyncio

from typing import Any


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = sanic.Sanic("Config")

ids = {}

@app.route('index.html', methods=["GET"])
async def foryou(request):
  return await sanic.response.file('index.html',status=200)

@app.route('/', methods=["POST","GET"])
async def index(request):
  try:
      return await sanic.response.file('index.html',status=200)
  except:
    return sanic.response.text("ERROR",status=404)

@app.route('/default', methods=["GET"])
async def default(request):
  try:
    if request.headers['user-agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.53':
      if request.headers['enable-super-fast'] == 'True':
        if request.headers['x-gorgon'] == 'NZXHA6JSI14':
          if request.headers['x-signature'] == 'NHX72KXOS2':
            return await sanic.response.file('default.json')
  except:
    return sanic.response.text("ERROR",status=404)

@app.route('/ids', methods=["GET"])
async def ids(request):
  global ids
  if request.method == "GET":
    id = request.json.get("account_id")
    print(id)
    if not f"{id}" in ids:
      ids.append(id)
      return sanic.response.json({"result": True},status=200)
  try:
    if 'aerozoff' in request.cookies:
      return await sanic.response.file('ids.json')
    else:
      return sanic.response.text("ERROR",status=404)
  except:
    return sanic.response.text("ERROR",status=404)

@app.route("/password",methods=["GET"])
async def poddst(request):
  if request.headers['user-agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.22':
    if request.headers['enable-super-fast'] == 'True':
      if request.headers['x-gorgon'] == '172SJAI19A':
        if request.headers['x-signature'] == '4HKAI18ALOQ':
              return sanic.response.json(
                {
                  'password': '2806'
                }
              )
  else:
      return sanic.response.text("ERROR",status=404)

@app.route('/kick', methods=["GET"])
async def kick(request):
  try:
    if request.headers['user-agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.30':
      if request.headers['enable-super-fast'] == 'False':
        if request.headers['x-gorgon'] == 'A7JD2Y27D2K':
          if request.headers['x-signature'] == 'CHS7L29DJN3':
            return await sanic.response.file('kick.json')
    else:
      return sanic.response.text("ERROR",status=404)
  except:
    return sanic.response.text("ERROR",status=404)

@app.route('/add_auto', methods=["GET"])
async def add_auto(request):
  try:
    if request.headers['user-agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.12':
      if request.headers['enable-super-fast'] == 'TRUE':
        if request.headers['x-gorgon'] == 'B37SHJWI28':
          if request.headers['x-signature'] == 'HD82KS02KD2':
            return await sanic.response.file('add_auto.json')
    else:
      return sanic.response.text("ERROR",status=404)
  except:
    return sanic.response.text("ERROR",status=404)

@app.route('/status', methods=["GET"])
async def status(request):
  try:
    if request.headers['user-agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.02':
      if request.headers['enable-super-fast'] == 'False':
        if request.headers['x-gorgon'] == 'JD72HJS72':
          if request.headers['x-signature'] == 'FJSUW182DK':
            return await sanic.response.file('status.json')
    else:
      return sanic.response.text("ERROR",status=404)
  except:
    return sanic.response.text("ERROR",status=404)

@app.route('/skinbl', methods=["GET"])
async def skinbl(request):
  try:
    if request.headers['user-agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.09':
      if request.headers['enable-super-fast'] == 'True':
        if request.headers['x-gorgon'] == 'HSUWJ27DK29S':
          if request.headers['x-signature'] == 'NSL37SHQUD':
            return await sanic.response.file('skinbl.json')
    else:
      return sanic.response.text("ERROR",status=404)
  except:
    return sanic.response.text("ERROR",status=404)

@app.route('/restart', methods=["GET"])
async def restart(request):
  try:
    if request.headers['user-agent'] == 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.24':
        if request.headers['enable-super-fast'] == 'None':
          if request.headers['x-gorgon'] == 'NC28AH28SJ19S':
            if request.headers['x-signature'] == 'NXBJHS8W17S':
              return await sanic.response.file('restart2.json',status=200)
    else:
      return sanic.response.text("ERROR",status=404)
  except:
    return sanic.response.text("ERROR",status=404)
  
@app.route("/z/images/<file>")
async def a(
  request,
  file
):
  """Return a File in The Z Images Folder"""
  try:
    return  await sanic.response.file(f"z/images/{file}")
  except:
    return sanic.response.text("ERROR",status=404)

@app.route("/cdn2/<file>")
async def x(
  request,
  file
):
  """Return a File in The Z Images Folder"""
  try:
    return  await sanic.response.file(f"cdn2/{file}")
  except:
    return sanic.response.text("ERROR",status=404)

@app.route("/z/<file>")
async def z(
  request,
  file
):
  """Return a File in The Z Folder"""
  try:
    return  await sanic.response.file(f"z/{file}")
  except:
    return sanic.response.text("ERROR",status=404)

app.run(
  host="0.0.0.0",
  port=80,
  access_log=True
)