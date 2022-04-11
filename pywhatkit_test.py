import pywhatkit
import time
import pyautogui
import keyboard

# Send a WhatsApp Message to a Contact at 1:30 PM
# pywhatkit.sendwhatmsg("+5511997965532", "teste", 12, 52)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
#pywhatkit.sendwhatmsg("+5511997965532", "Hi", 13, 6, 10, True, 2)
for i in range(10):
    time.sleep(1)
    print(i)
print("executando enter")
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')



# # Send an Image to a Group with the Caption as Hello
# pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# # Send an Image to a Contact with the no Caption
# pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# # Send a WhatsApp Message to a Group at 12:00 AM
# pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# # Send a WhatsApp Message to a Group instantly
# pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# # Play a Video on YouTube
# pywhatkit.playonyt("PyWhatKit")