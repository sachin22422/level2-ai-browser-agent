from fastapi import Body
from fastapi.responses import JSONResponse
from app.browser_control import perform_action

async def interact_route(command: str = Body(..., embed=True)):
    print(f"📥 Received command: {command}")
    try:
        result = perform_action(command)
        print(f"✅ perform_action result: {result}")
        return JSONResponse(content={"status": "success", "message": result})
    except Exception as e:
        print("❌ Error during /interact:")
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=500, content={"status": "error", "message": str(e)})
