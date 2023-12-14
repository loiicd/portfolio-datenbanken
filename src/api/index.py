import uvicorn

def runApiClient(workers: int, dev: bool):
  uvicorn.run('apiHandler:app' ,host='127.0.0.1', reload=dev, port=8000, workers=workers)

if __name__=='__main__':
  runApiClient(10, True)