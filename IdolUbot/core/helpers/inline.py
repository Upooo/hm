from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import *
from pyromod.helpers import ikb
from IdolUbot import *


def detect_url_links(text):
    link_pattern = (
        r"(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]{2,})+(?:[/?]\S+)?"
    )
    link_found = re.findall(link_pattern, text)
    return link_found


def detect_button_and_text(text):
    button_matches = re.findall(r"\| ([^|]+) - ([^|]+) \|", text)
    text_matches = (
        re.search(r"(.*?) \|", text, re.DOTALL).group(1) if "|" in text else text
    )
    return button_matches, text_matches


def create_inline_keyboard(text, user_id=False, is_back=False):
    keyboard = []
    button_matches, text_matches = detect_button_and_text(text)

    prev_button_data = None
    for button_text, button_data in button_matches:
        data = (
            button_data.split("#")[0]
            if detect_url_links(button_data.split("#")[0])
            else f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]} {button_data.split('#')[0]}"
        )
        cb_data = data if user_id else button_data.split("#")[0]
        if "#" in button_data:
            if prev_button_data:
                if detect_url_links(cb_data):
                    keyboard[-1].append(InlineKeyboardButton(button_text, url=cb_data))
                else:
                    keyboard[-1].append(
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    )
            else:
                if detect_url_links(cb_data):
                    button_row = [InlineKeyboardButton(button_text, url=cb_data)]
                else:
                    button_row = [
                        InlineKeyboardButton(button_text, callback_data=cb_data)
                    ]
                keyboard.append(button_row)
        else:
            if button_data.startswith("http"):
                button_row = [InlineKeyboardButton(button_text, url=cb_data)]
            else:
                button_row = [InlineKeyboardButton(button_text, callback_data=cb_data)]
            keyboard.append(button_row)

        prev_button_data = button_data

    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    if user_id and is_back:
        markup.inline_keyboard.append(
            [
                InlineKeyboardButton(
                    "ᴋᴇᴍʙᴀʟɪ",
                    f"_gtnote {int(user_id.split('_')[0])}_{user_id.split('_')[1]}",
                )
            ]
        )

    return markup, text_matches


class BTN:
    def ALIVE(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="ᴛᴜᴛᴜᴘ",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ],
            [
                InlineKeyboardButton(
                    text="ʜᴇʟᴘ",
                    callback_data="help_back",
                )
            ]
        ]
        return button

    def BOT_HELP(message):
        button = [
            [InlineKeyboardButton("ʀᴇsᴛᴀʀᴛ", callback_data="reboot")],
            [InlineKeyboardButton("ꜱʏꜱᴛᴇᴍ", callback_data="system")],
            [InlineKeyboardButton("ᴜʙᴏᴛ", callback_data="ubot")],
            [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", callback_data="update")],
        ]
        return button
        
    def ADD_EXP(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} ʙᴜʟᴀɴ ",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(
            InlineKeyboardButton(
                "ᴅᴀᴘᴀᴛᴋᴀɴ ᴘʀᴏfɪʟ", callback_data=f"profil {user_id}"
            )
        )
        buttons.row(
            InlineKeyboardButton(
                "ᴛᴏʟᴀᴋ ᴘᴇᴍʙᴀʏᴀʀᴀɴ", callback_data=f"failed {user_id}"
            )
        )
        return buttons

    def EXP_UBOT():
        button = [
            [InlineKeyboardButton("ʙᴜʏ ᴜʙᴏᴛ", callback_data="bahan")],
        ]
        return button

    
    def START(message):
        if not message.from_user.id == OWNER_ID:
            button = [
                [
                    InlineKeyboardButton("ʙᴜʏ ᴜʙᴏᴛ", callback_data="bahan"),
                ], 
                [
                    InlineKeyboardButton("ᴛʀɪᴀʟ", callback_data="trial_ubot"),
                    InlineKeyboardButton("ғɪᴛᴜʀ", callback_data="help_back")
                ],
                [
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="informasi_ubot"),
                ],
                [   
                    InlineKeyboardButton("ᴄʀᴇᴀᴛᴇ ᴜʙᴏᴛ", callback_data="buat_ubot"),
                ]
            ]
        else:
            button = [
                [
                    InlineKeyboardButton("ꜱᴛᴀʀᴛ ᴄʀᴇᴀᴛɪɴɢ", callback_data="bahan")
                ],
                [
                    InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ", callback_data="cb_gitpull"),
                    InlineKeyboardButton("ʀᴇsᴛᴀʀᴛ", callback_data="cb_restart")
                ],
                [
                    InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="informasi_ubot")
                ],
                [
                    InlineKeyboardButton("ʟɪsᴛ ᴜsᴇʀ", callback_data="cek_ubot")
                ],
                [
                    InlineKeyboardButton("ғɪᴛᴜʀ", callback_data="help_back")
                ]
            ]
        return button

    def PLUS_MINUS(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("ᴄᴏɴꜰɪʀᴍ", callback_data="confirm")],
            [InlineKeyboardButton("ᴄᴀɴᴄᴇʟ", callback_data=f"home {user_id}")],
        ]
        return button

    
    def UBOT(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ɢᴇᴛ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ɢᴇᴛ ᴄᴏᴅᴇ ᴏᴛᴘ",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ɢᴇᴛ ᴄᴏᴅᴇ 𝟸ғᴀ",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ", callback_data=f"ub_deak {int(count)}"
                )
            ],
            [
                InlineKeyboardButton("<", callback_data=f"p_ub {int(count)}"),
                InlineKeyboardButton(">", callback_data=f"n_ub {int(count)}"),
            ],
        ]
        return button

    def DEAK(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "ʙᴀᴄᴋ",
                    callback_data=f"p_ub {int(count)}"
                ),
                InlineKeyboardButton(
                    "ᴄᴏɴꜰɪʀᴍ", callback_data=f"deak_akun {int(count)}",
                ),
            ],
        ]
        return button
    def PLUS_MINUS(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("ᴄᴏɴꜰɪʀᴍ", callback_data="confirm")],
            [InlineKeyboardButton("ᴄᴀɴᴄᴇʟ", callback_data=f"home {user_id}")],
        ]
        return button

    
    def UBOT(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "ʜᴀᴘᴜs ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀsᴇ",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ɢᴇᴛ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ",
                    callback_data=f"get_phone {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ᴄᴇᴋ ᴍᴀsᴀ ᴀᴋᴛɪғ",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ɢᴇᴛ ᴄᴏᴅᴇ ᴏᴛᴘ",
                    callback_data=f"get_otp {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ɢᴇᴛ ᴄᴏᴅᴇ 𝟸ғᴀ",
                    callback_data=f"get_faktor {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛ", callback_data=f"ub_deak {int(count)}"
                )
            ],
            [
                InlineKeyboardButton("<", callback_data=f"p_ub {int(count)}"),
                InlineKeyboardButton(">", callback_data=f"n_ub {int(count)}"),
            ],
        ]
        return button

    def DEAK(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "ʙᴀᴄᴋ",
                    callback_data=f"p_ub {int(count)}"
                ),
                InlineKeyboardButton(
                    "ᴄᴏɴꜰɪʀᴍ", callback_data=f"deak_akun {int(count)}",
                ),
            ],
        ]
        return button
