from aiohttp import web
import json
import aiofiles
import aiofiles.os as aios
import os

async def save_json(account_login, data):
    await aios.makedirs('terminals', exist_ok=True)
    file_name = os.path.join('terminals', f'{account_login}.json')

    async with aiofiles.open(file_name, 'w') as file:
        await file.write(json.dumps(data, indent=4))

async def handle_post(request):
    # Get the account_login parameter from the URL
    account_login = request.match_info.get('account_login', "Anonymous")
    print("Account Login:", account_login)

    try:
        # Parse JSON payload from the request
        data = await request.json()
        print("Received data:", data)

        # Create a response dictionary
        response_data = {
            "status": "success",
            "message": f"Data received for account {account_login}",
            "received_data": data
        }

        await save_json(account_login, data)

        # Send the JSON response
        return web.json_response(response_data)

    except json.JSONDecodeError:
        # Handle JSON decoding error
        return web.json_response({
            "status": "error",
            "message": "Invalid JSON payload"
        }, status=400)

async def fetch_json(account_login):
        # Use os.path.join to construct the file path
        file_name = os.path.join('terminals', f'{account_login}.json')

        # Check if the file exists
        if not os.path.exists(file_name):
            return None

        # Read the JSON data from the file asynchronously
        async with aiofiles.open(file_name, 'r') as file:
            contents = await file.read()
            return json.loads(contents)
   


async def handle_fetch(request):
    try:
        account_login = request.match_info.get('account_login')
        
        data = await fetch_json(account_login)

        if data is None:
            return web.json_response({"status": "error", "message": "File not found"}, status=404)

        return web.json_response({"status": "success", "data": data})
    except OSError:
        return web.json_response({"status": "failed", "data": f"Trades data for {account_login} being updated. Please retry."})
    except Exception:
        return web.json_response({"status": "failed", "data": "Some error occured. Please retry."})

# Initialize the app and add the route with a URL parameter
app = web.Application()
app.router.add_post('/trades/{account_login}', handle_post)
app.router.add_get('/fetch/{account_login}', handle_fetch)

# Run the app
if __name__ == '__main__':
    web.run_app(app, port=8080)
