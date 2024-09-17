### FastAPI: A Modern Python Web Framework

---

![FastAPI](images/fastapi.png)

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. FastAPI helps developers build efficient, scalable APIs quickly with automatic interactive API documentation.

#### Features of FastAPI:
- **Fast**: Very high performance, on par with Node.js and Go.
- **Easy to Use**: Designed to be easy to learn and use.
- **Data validation**: Automatic validation and serialization using Pydantic.
- **Interactive API docs**: Comes with OpenAPI and ReDoc out of the box.

#### Example: Simple FastAPI App

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

This small example creates an API that responds with `{"Hello": "World"}` when you access the root endpoint.

#### Resources to Learn FastAPI
- [Official Documentation](https://fastapi.tiangolo.com/)
- [GitHub Repo](https://github.com/tiangolo/fastapi)