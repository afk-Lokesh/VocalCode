from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Command(BaseModel):
    command_text: str

@router.post("/execute")
def execute_command(cmd: Command):
    text = cmd.command_text.lower()
    if 'run python' in text:
        return {'action': 'RUN_PYTHON'}
    elif 'format code' in text:
        return {'action': 'FORMAT'}
    else:
        return {'action': 'UNKNOWN'}

