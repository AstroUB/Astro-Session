# AstroUB
# ASTRO-UB

import os
from time import sleep

print("")
a = r"""
© ASTRO-USERBOT ©
╔═══╦═══╦════╦═══╦═══╗
║╔═╗║╔═╗║╔╗╔╗║╔═╗║╔═╗║
║║─║║╚══╬╝║║╚╣╚═╝║║─║║
║╚═╝╠══╗║─║║─║╔╗╔╣║─║║
║╔═╗║╚═╝║─║║─║║║╚╣╚═╝║
╚╝─╚╩═══╝─╚╝─╚╝╚═╩═══╝
•Secure Bot•
~ ASTRO UserBot ~
"""


def spinner():
    print("Checking setup of TELETHON...")
    for _ in range(3):
        for frame in r"-\|/-\|/":
            print("\b", frame, sep="", end="", flush=True)
            sleep(0.1)


def clear_screen():
    if os.name == "posix":
        os.system("clear")
    else:
        # for windows platfrom
        os.system("cls")


def get_api_id_and_hash():
    print(
        "Get your API ID and API HASH from my.telegram.org or @Api_ScrapperRoBot to proceed.\n\n",
    )
    try:
        API_ID = int(input("Enter API ID: "))
    except ValueError:
        print("APP ID must be an integer.\nQuitting...")
        exit(0)
    API_HASH = input("Enter API HASH: ")
    return API_ID, API_HASH


def telethon_session():
    try:
        spinner()

        x = "\bFound an existing installation of Telethon...\nSuccessfully Imported.\n\n"
    except BaseException:
        print("Installing Telethon...")
        os.system("pip install -U telethon")

        x = "\bDone. Installed and imported Telethon."
    clear_screen()
    print("Welcome There✨")
    print("This is String Session Generator")
    print("For Terminals 😙")
  
    print(x)

    # the imports

    from telethon.errors.rpcerrorlist import ApiIdInvalidError, PhoneNumberInvalidError
    from telethon.sessions import StringSession
    from telethon.sync import TelegramClient

    API_ID, API_HASH = get_api_id_and_hash()

    # logging in
    try:
        with TelegramClient(StringSession(), API_ID, API_HASH) as barsha:
            print("Generating Your String Session😙To run Astro🤩")
            adi = barsha.send_message(
                "me",
                f"**ASTRO** `SESSION`:\n\n`{barsha.session.save()}`\n\n**Do not share this anywhere!**",
            )
            adi.reply("The Above is the your `STRING_SESSION` FOR your **AstroUB**\n__Thanks For Using AstroUB❤️__\n\n For any kind of Help Join ~ @Astro_HelpChat")
            print(
                "Your SESSION has been generated Successfully to run Astro\nYou can't copy from here😅\nCheck Your Saved Message in Telegram 😙🤩"
            )
            exit(0)
    except ApiIdInvalidError:
        print(
            "Your API ID/API HASH combination is invalid. Kindly recheck.\nStop Progress\nExiting...."
        )
        exit(0)
    except ValueError:
        print("API HASH must not be empty!\nStop Progress\nExiting....")
        exit(0)
    except PhoneNumberInvalidError:
        print("The phone number is invalid!\nStoping Progress\nExiting...")
        exit(0)


def main():
    clear_screen()
    print(a)
    telethon_session()
    x = input("Run again? (y/n")
    if x == "y":
        main()
    else:
        exit(0)


main()
