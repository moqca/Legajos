#!/usr/bin/env python
#Boa:App:BoaApp
import wxversion
wxversion.select('2.9')

import wx

import mainWindow
import splash

modules ={u'financial_parser': [0, '', u'financial_parser.py'],
 u'mainWindow': [1, 'Main frame of Application', u'mainWindow'],
 u'project_handle': [0, '', u'../project_handle.py']}
'''
class BoaApp(wx.App):
    def OnInit(self):
        self.main = mainWindow.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True
'''
class BoaApp(wx.App):
	def OnInit(self):
		self.main = splash.MySplashScreen()
		self.main.Show()
		self.SetTopWindow(self.main)
		return True
		
def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
