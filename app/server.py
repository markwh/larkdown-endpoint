from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from larkdown_chat.chain import chain as larkdown_chat_chain


app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, larkdown_chat_chain, path="/larkdown-chat")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
