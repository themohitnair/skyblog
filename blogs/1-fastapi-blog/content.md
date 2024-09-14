# Getting Started with FastAPI: Building Efficient APIs in Python

![FastAPI Logo](images/fastapi-logo.png)

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints. It's designed to be easy to use, fast to code, ready for production, and suitable for building robust and scalable applications.

## Key Features of FastAPI

1. **Fast**: Very high performance, on par with NodeJS and Go.
2. **Fast to code**: Increase the speed to develop features by about 200% to 300%.
3. **Fewer bugs**: Reduce about 40% of human (developer) induced errors.
4. **Intuitive**: Great editor support. Completion everywhere. Less time debugging.
5. **Easy**: Designed to be easy to use and learn. Less time reading docs.
6. **Short**: Minimize code duplication. Multiple features from each parameter declaration.
7. **Robust**: Get production-ready code. With automatic interactive documentation.
8. **Standards-based**: Based on (and fully compatible with) the open standards for APIs: OpenAPI and JSON Schema.

## Quick Start

Here's a simple example of a FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

To run this application, save it as `main.py` and execute:

```
uvicorn main:app --reload
```

Visit `http://localhost:8000/docs` to see the automatic interactive API documentation.

## Conclusion

FastAPI makes it easy to build robust and efficient APIs quickly. Its automatic documentation, type checking, and high performance make it an excellent choice for modern API development in Python.