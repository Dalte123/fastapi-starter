from fastapi import Depends, HTTPException, Header
import os
TOKEN = os.getenv("APP_TOKEN", "superSecret123")




def authfunc(authorization: str = Header(None)) -> str:
	if authorization is None:
		raise HTTPException(status_code=401, detail="Token was not sent")
	elif not authorization.startswith("Bearer "):
		raise HTTPException(status_code=400, detail="Token does not start with Bearer")
	else:
		password = authorization.split()[-1]
		
		if password == TOKEN:
			return True 
		else:
			raise HTTPException(status_code=401, detail="Unauthorized")	
					
