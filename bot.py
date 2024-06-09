import logging, asyncio

from os import environ
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

logging.basicConfig(level=logging.ERROR)
       
SESSION = environ.get("SESSION", "BQFLjmAAY1CUBUSdrU8dJxF08E7nk9lREirK9KIvf_iuyB6IpuWR1ofIZ8ZLVPmDCoVuy7ghoBtlz6sFNBN09xmeylRaksCVq_n4wom-qmd6uswCuYMX4qHYWsTtWgjDF1Z2q4Bpp3CVjb-zdizcf42kI9e5CZlVWuxok3zrgbKtTpUxut-T-Uh7VFAEoD4LmZ6FngSEA4MScRF6o1xE9bUeL3P52T98rJShs5qRMhyl6qEyTL1DoHcxaYCpxCOwv_yHDnXIaMt4ddwllF1AhDH9kOSVtiwIlpaMrlOxgzkOcoCjjpsh4r7lgzFanm0ndoXx5W4yEuHs9bQOmH_4Wsdae12segAAAAGrMHFgAA")        
User = Client(name="AcceptUser", session_string=SESSION)


@User.on_message(filters.command(["run", "approve"], [".", "/"]))                     
async def approve(client, message):
    Id = message.chat.id
    await message.delete(True)
 
    try:
       while True: # create loop is better techniq to accept within seconds 💀
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))
    except FloodWait as s:
        asyncio.sleep(s.value)
        while True:
           try:
               await client.approve_all_chat_join_requests(Id)         
           except FloodWait as t:
               asyncio.sleep(t.value)
               await client.approve_all_chat_join_requests(Id) 
           except Exception as e:
               logging.error(str(e))

    msg = await client.send_message(Id, "**Task Completed** ✓ **Approved Pending All Join Request**")
    await msg.delete()


logging.info("Bot Started....")
User.run()







