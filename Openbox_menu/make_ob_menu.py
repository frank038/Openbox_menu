#!/usr/bin/env python3
# tested with Openbox v. 3.6.1

import pop_menu
a = pop_menu.getMenu()
menu = a.retList()[0]

# extended categories
development_extended_categories = ["Building","Debugger","IDE","GUIDesigner",
                                  "Profiling","RevisionControl","Translation",
                                  "Database","WebDevelopment"]

office_extended_categories = ["Calendar","ContanctManagement","Office",
                             "Dictionary","Chart","Email","Finance","FlowChart",
                             "PDA","ProjectManagement","Presentation","Spreadsheet",
                             "WordProcessor","Engineering"]

graphics_extended_categories = ["2DGraphics","VectorGraphics","RasterGraphics",
                               "3DGraphics","Scanning","OCR","Photography",
                               "Publishing","Viewer"]

utility_extended_categories = ["TextTools","TelephonyTools","Compression",
                              "FileTools","Calculator","Clock","TextEditor",
                              "Documentation"]

settings_extended_categories = ["DesktopSettings","HardwareSettings",
                               "Printing","PackageManager","Security",
                               "Accessibility"]

network_extended_categories = ["Dialup","InstantMessaging","Chat","IIRCClient",
                              "FileTransfer","HamRadio","News","P2P","RemoteAccess",
                              "Telephony","VideoConference","WebBrowser"]

# added "Audio" and "Video" main categories
audiovideo_extended_categories = ["Audio","Video","Midi","Mixer","Sequencer","Tuner","TV",
                                 "AudioVideoEditing","Player","Recorder",
                                 "DiscBurning"]

game_extended_categories = ["ActionGame","AdventureGame","ArcadeGame",
                           "BoardGame","BlockGame","CardGame","KidsGame",
                           "LogicGame","RolePlaying","Simulation","SportGame",
                           "StrategyGame","Amusement","Emulator"]

education_extended_categories = ["Art","Construction","Music","Languages",
                                "Science","ArtificialIntelligence","Astronomy",
                                "Biology","Chemistry","ComputerScience","DataVisualization",
                                "Economy","Electricity","Geography","Geology","Geoscience",
                                "History","ImageProcessing","Literature","Math","NumericAnalysis",
                                "MedicalSoftware","Physics","Robots","Sports","ParallelComputing",
                                "Electronics"]

system_extended_categories = ["FileManager","TerminalEmulator","FileSystem",
                             "Monitor","Core"]

# main categories
AudioVideo = []
Development = []
Education = []
Game = []
Graphics = []
Network = []
Office = []
Settings = []
System = []
Utility = []
Missed = []
#
for el in menu:
    cat = el[2]
    if cat == "AudioVideo" or cat in audiovideo_extended_categories:
        # label - executable - icon
        AudioVideo.append([el[0],el[4],el[5]])
    elif cat == "Development" or cat in development_extended_categories:
        Development.append([el[0],el[4],el[5]])
    elif cat == "Education" or cat in education_extended_categories:
        Education.append([el[0],el[4],el[5]])
    elif cat == "Game" or cat in game_extended_categories:
        Game.append([el[0],el[4],el[5]])
    elif cat == "Graphics" or cat in graphics_extended_categories:
        Graphics.append([el[0],el[4],el[5]])
    elif cat == "Network" or cat in network_extended_categories:
        Network.append([el[0],el[4],el[5]])
    elif cat == "Office" or cat in office_extended_categories:
        Office.append([el[0],el[4],el[5]])
    elif cat == "Settings" or cat in settings_extended_categories:
        Settings.append([el[0],el[4],el[5]])
    elif cat == "System" or cat in system_extended_categories:
        System.append([el[0],el[4],el[5]])
    elif cat == "Utility" or cat in utility_extended_categories:
        Utility.append([el[0],el[4],el[5]])
    else:
        Missed.append([el[0],el[4],el[5]])

# top
print('<?xml version="1.0" encoding="UTF-8"?>\n<openbox_menu>\n    <menu id="root-menu" label="OpenBox 3">')
#
i = 1
# categories and applications
if AudioVideo:
    print('        <menu id="{}" label="AudioVideo"> '.format(i))
    i += 1
    for el in AudioVideo:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Development:
    print('        <menu id="{}" label="Development"> '.format(i))
    i += 1
    for el in Development:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Education:
    print('        <menu id="{}" label="Education"> '.format(i))
    i += 1
    for el in Education:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Game:
    print('        <menu id="{}" label="Game"> '.format(i))
    i += 1
    for el in Game:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Graphics:
    print('        <menu id="{}" label="Graphics"> '.format(i))
    i += 1
    for el in Graphics:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Network:
    print('        <menu id="{}" label="Network"> '.format(i))
    i += 1
    for el in Network:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Office:
    print('        <menu id="{}" label="Office"> '.format(i))
    i += 1
    for el in Office:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Settings:
    print('        <menu id="{}" label="Settings"> '.format(i))
    i += 1
    for el in Settings:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if System:
    print('        <menu id="{}" label="System"> '.format(i))
    i += 1
    for el in System:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Utility:
    print('        <menu id="{}" label="Utility"> '.format(i))
    i += 1
    for el in Utility:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

if Missed:
    print('        <menu id="{}" label="Missed"> '.format(i))
    i += 1
    for el in Missed:
        print('            <item label="{}"> <action name="Execute">\n                <execute>{}</execute>\n            </action> </item>'.format(el[0],el[1]))
    print('        </menu>')

# openbox menu
print('        <separator/>\n        <menu id={} label="OpenBox">\n            <menu id="client-list-menu"/>\n            <item label="Reconfigure"> <action name="Reconfigure"/> </item>\n            <separator/>\n            <item label="Exit"> <action name="Exit"/> </item>\n        </menu>'.format(i+1))


# bottom
print("    </menu>\n</openbox_menu>")

