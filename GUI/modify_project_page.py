# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class modify_project
###########################################################################

class modify_project ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Modify Project...", pos = wx.DefaultPosition, size = wx.Size( 505,350 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Project Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.input_project_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.input_project_name, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Description (Optional)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		bSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.input_project_description = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE )
		bSizer2.Add( self.input_project_description, 1, wx.ALL|wx.EXPAND, 5 )

		self.chk_isFinished = wx.CheckBox( self, wx.ID_ANY, u"This project has been finished", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.chk_isFinished, 0, wx.ALL, 5 )

		btn_ok = wx.StdDialogButtonSizer()
		self.btn_okOK = wx.Button( self, wx.ID_OK )
		btn_ok.AddButton( self.btn_okOK )
		self.btn_okCancel = wx.Button( self, wx.ID_CANCEL )
		btn_ok.AddButton( self.btn_okCancel )
		btn_ok.Realize();

		bSizer2.Add( btn_ok, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.get_value )
		self.btn_okCancel.Bind( wx.EVT_BUTTON, self.close_window )
		self.btn_okOK.Bind( wx.EVT_BUTTON, self.modify_project )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def get_value( self, event ):
		event.Skip()

	def close_window( self, event ):
		event.Skip()

	def modify_project( self, event ):
		event.Skip()


