#---------------------------
#   Import Libraries
#---------------------------
import os
import sys
import json
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) #point at lib folder for classes / references

import clr
clr.AddReference("IronPython.SQLite.dll")
clr.AddReference("IronPython.Modules.dll")

#   Import your Settings class
from Settings_Module import MySettings
#---------------------------
#   [Required] Script Information
#---------------------------
ScriptName = "Template Script"
Website = "https://www.streamlabs.com"
Description = "!test will post a message in chat"
Creator = "AnkhHeart"
Version = "1.0.0.0"

#---------------------------
#   Define Global Variables
#---------------------------
global SettingsFile
SettingsFile = os.path.join(os.path.dirname(__file__), "Settings\settings.json")
global ScriptSettings
ScriptSettings = MySettings(SettingsFile)

#---------------------------
#   [Required] Initialize Data (Only called on load)
#---------------------------
def Init():
    ScriptSettings.Response = "Overwritten pong! ^_^"
    return

#---------------------------
#   [Required] Execute Data / Process messages
#---------------------------
def Execute(data):

    #   Check if the propper command is used, the command is not on cooldown and the user has permission to use the command
    if data.IsChatMessage() and data.GetParam(0).lower() == ScriptSettings.Command and not Parent.IsOnCooldown(ScriptName,ScriptSettings.Command) and Parent.HasPermission(data.User,ScriptSettings.Permission,ScriptSettings.Info):
        Parent.SendStreamMessage(ScriptSettings.Response)    # Send your message to chat
        Parent.AddCooldown(ScriptName,ScriptSettings.Command,ScriptSettings.Cooldown)  # Put the command on cooldown
    return

#---------------------------
#   [Required] Tick method (Gets called during every iteration even when there is no incoming data)
#---------------------------
def Tick():
    return

#---------------------------
#   [Optional] Parse method (Allows you to create your own custom $parameters) 
#---------------------------
def Parse(parseString, userid, username, targetid, targetname, message):
    
    if "$myparameter" in parseString:
        return parseString.replace("$myparameter","I am a cat!")
    
    return parseString

#---------------------------
#   [Optional] Reload Settings (Called when a user clicks the Save Settings button in the Chatbot UI)
#---------------------------
def ReloadSettings(jsonData):
    # Execute json reloading here
    ScriptSettings.__dict__ = json.loads(jsonData)
    ScriptSettings.Save(SettingsFile)
    return

#---------------------------
#   [Optional] Unload (Called when a user reloads their scripts or closes the bot / cleanup stuff)
#---------------------------
def Unload():
    return

#---------------------------
#   [Optional] ScriptToggled (Notifies you when a user disables your script or enables it)
#---------------------------
def ScriptToggled(state):
    return