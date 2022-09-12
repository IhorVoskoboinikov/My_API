import uvicorn


uvicorn.run(
    'test_project.app:app',
    reload=True
)
