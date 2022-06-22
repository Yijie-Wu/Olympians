import uvicorn
from loguru import logger

from app import create_app

app = create_app()

if __name__ == '__main__':
    # development only
    host = 'localhost'
    port = 9000
    logger.info(f'Running on http://{host}:{port}')
    logger.info(f'API documentation: http://{host}:{port}/docs')
    uvicorn.run(app='main:app', host=host, port=port, reload=True, debug=True)
