import requests

token = "MTE1MTM4NjgwMTczMTI3Njg2MA.Gj5pnZ.vwzCP4wxXuT-Gl2DH130kSyMM8tcmR8imAOJ4E"

def selfbottingquestionmark(): # i dont think i need this function but whatever
    selfbot = input(r"Are you selfbotting? (yes\no): ")
    if selfbot == "yes":
        headers = {"Authorization": f"{token}"}
        main(headers)
    elif selfbot == "no":
        headers = {"Authorization": f"Bot {token}"}
        main(headers)
    else:
        print("Please enter a correct answer")
        selfbottingquestionmark()


def clone_channel(headers):
    source_channel_id = input("Source Channel ID: ")
    target_guild_id = input("Target Guild ID: ")    
    source_channel_url = f"https://discord.com/api/v9/channels/{source_channel_id}"
    response = requests.get(source_channel_url, headers=headers)
    source_channel_data = response.json()

    remove = ["last_message_id", "guild_id", "parent_id", "position", "permission_overwrites", "id"] # removed data(for example 'last_message_id' you cant create a channel with that json data)
    for key in remove:
        source_channel_data.pop(key, None)
    
    source_guild_url = f"https://discord.com/api/v9/guilds/{target_guild_id}/channels"
    response = requests.post(source_guild_url, headers=headers, json=source_channel_data)
    target_channel_data = response.json()

    if response.status_code == 201:
        print(f"Channel cloned successfully. New channel ID: {target_channel_data['id']}")
    else:
        print(f"Failed to clone channel. Status code: {response.status_code}")# :(

def clone_role(headers):
    target_guild_id = input("Target Guild ID: ")
    source_role_id = input("Source Role ID: ")
    source_guild_url = f'https://discord.com/api/v9/guilds/{target_guild_id}/roles'
    response = requests.get(source_guild_url, headers=headers)
    
    if response.status_code == 200:
        source_role_data = response.json()
        
        for role in source_role_data:
            if role['id'] == source_role_id:
                print("Found role:")
                print(role)
                remove = ["position", "icon", "unicode_emoji", "tags", "flags", "managed", "id"] # removed data(for example 'unicode_emoji' you cant create a role with that json data if you dont have levvel 2+ boost)
                for key in remove:
                    role.pop(key, None)
                response2 = requests.post(f"https://discord.com/api/v9/guilds/{target_guild_id}/roles", headers=headers, json=role)
                if response2.status_code == 200:
                    print("Cloned role successfully!")
                else:
                    print(f"Error cloning role response: {response2.status_code}") # :(
                return role
                



def main(headers):
    while True:
        print("option 1: clone channel \noption 2: clone role \nmade by github.com/dropalways this is ass rn i will hopefully make it better :)") # lie and give false hope
        choice = input("pick num ")
        if choice == "1":
            clone_channel(headers)
        elif choice == "2":
            clone_role(headers)
        else:
            print("dumbass not a option")

selfbottingquestionmark()
