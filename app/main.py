from fastapi import FastAPI

app = FastAPI(title='InferPilot')

@app.get('/')
async def healthcheck():
    return {'service': 'inferpilot', 'status': 'healthy'}
